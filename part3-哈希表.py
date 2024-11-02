#2024-10-28
#哈希表的三种数据结构: 数组、set、map

#set: 底层实现: 红黑树; 有序; 数值不可重复、不可更改; 查询: O(logn); 增删: O(logn)
#multiset: 底层实现: 红黑树; 有序; 数值可重复、不可更改; 查询: O(logn); 增删: O(logn)
#unordered_set: 底层实现: 哈希表; 无序; 数值不可重复、不可更改; 查询: O(1); 增删: O(1)
#当要使用集合来解决哈希问题的时候，优先使用unordered_set，因为它的查询和增删效率是最优的; 如果需要集合是有序的，那么就用set; 如果要求不仅有序还要有重复数据的话，那么就用multiset

#map: 底层实现: 红黑树; 有序; key不可重复、不可更改; 查询: O(logn); 增删: O(logn)
#multimap: 底层实现: 红黑树; 有序; key可重复、不可更改; 查询: O(logn); 增删: O(logn)
#unordered_map: 底层实现: 哈希表; 无序; key不可重复、不可更改; 查询: O(1); 增删: O(1)

#总结: 数值都不可更改; 其中用红黑树实现的都是有序, 时间为O(logn); 用哈希表实现的都是无序, 时间为O(1)

#哈希表1 - 有效的字母异位词 (LeetCode 242):
class Solution:
    def isAnagram(self, s, t):
        record = [0] * 26
        for i in s:
            record[ord(i) - ord("a")] += 1 #ord():返回字符的unicode值; 这里差值正好可以当作下标很巧妙
        for i in t:
            record[ord(i) - ord("a")] -= 1
        for i in range(26):
            if record[i] != 0:
                return False
        return True

#哈希表2 - 两个数组的交集 (LeetCode 349):
#方法一: 暴力解法: 时间复杂度O(n^2)
class Solution:
    def intersection(self, nums1, nums2):
        result = set()
        for element in nums1:
            if element in nums2:
                result.add(element)
        return list(result)
#方法二: 集合
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
#方法三:数组
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = [0]*1001
        count2 = [0]*1001
        result = []
        for i in range(len(nums1)):
            count1[nums1[i]]+=1
        for j in range(len(nums2)):
            count2[nums2[j]]+=1
        for k in range(1001):
            if count1[k]*count2[k]>0: #这里的比较思路类似上一题, 只不过这里是乘积>0, 上面是加减=0
                result.append(k)
        return result

#哈希表3 - 两数之和 (LeetCode 1):
#暴力O(n^2)很简单, 这里看一下怎么用哈希表做
#方法一: 字典
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = dict()

        for index, value in enumerate(nums):  
            if target - value in records:
                return [records[target- value], index]
            records[value] = index
        return []
#方法二: 集合
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()             
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [nums.index(complement), i]
            seen.add(num)

#哈希表4 - 四数相加II (LeetCode 454):
#用空间换时间, 把原本O(n^4)的问题转化为2个O(n^2)的问题
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        ab = {}
        result = 0
        for i in range(n):
            for j in range(n):
                if nums1[i] + nums2[j] not in ab.keys():
                    ab.update({nums1[i] + nums2[j]: 1})
                else:
                    ab[nums1[i] + nums2[j]] += 1
        for i in range(n):
            for j in range(n):
                if 0 - nums3[i] - nums4[j] in ab.keys():
                    result += ab[0 - nums3[i] - nums4[j]]
        return result

#哈希表5 - 三数之和 (LeetCode 15):
#初版: 有去重复, 但是超时了(通过了255/313个测试用例)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        dc = {}
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                else:
                    dc.update({(i,j): nums[i] + nums[j]})
        for k in range(n):
            for key in dc.keys():
                idx_i, idx_j = key
                val = dc[key]
                if 0 - nums[k] == val:
                    if k != idx_i and k != idx_j:
                        temp_list = [nums[idx_i], nums[idx_j], nums[k]]
                        temp_list.sort()
                        if temp_list not in result:
                            result.append(temp_list)
        return result
#改进版: 双指针(容易理解, 且去重不容易写错)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n):
            #如果第一个元素已经大于0(target)，不需要进一步检查
            if nums[i] > 0:
                return result
            #第1个元素去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1
            while right > left:
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else: #sum = 0(target)
                    result.append([nums[i], nums[left], nums[right]])
                    
                    #第2个元素去重
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1
                    #第3个元素去重        
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                       
                    left += 1
                    right -= 1
                
        return result

#哈希表6 - 四数之和 (LeetCode 18):
#类似题5的初版, 超时(通过221/294个测试用例)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        result = []
        dc = {}
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                else:
                    dc.update({(i,j): nums[i] + nums[j]})
        for k in range(n):
            for m in range(n):
                for key in dc.keys():
                    idx_i, idx_j = key
                    val = dc[key]
                    if target - nums[k] - nums[m] == val:
                        if k != idx_i and k != idx_j and k != m and m != idx_i and m != idx_j:
                            temp_list = [nums[idx_i], nums[idx_j], nums[k], nums[m]]
                            temp_list.sort()
                            if temp_list not in result:
                                result.append(temp_list)
        return result
#双指针(格式和题5基本一样, 只是多套了一层循环; 依此写法, 五数、六数等之和也可以解决, 需要O(n^(N-1))的时间复杂度)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]: 
        n = len(nums)
        nums.sort()
        result = []
        for i in range(n):
            #第1个元素去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1, n):
                #第2个元素去重
                if j > i+1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = n - 1
                while right > left:
                    if nums[j] + nums[left] + nums[right] > target - nums[i]:
                        right -= 1
                    elif nums[j] + nums[left] + nums[right] < target - nums[i]:
                        left += 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        #第3个元素去重
                        while right > left and nums[left] == nums[left + 1]:
                            left += 1
                        #第3个元素去重        
                        while right > left and nums[right] == nums[right - 1]:
                            right -= 1
                       
                        left += 1
                        right -= 1
        return result
