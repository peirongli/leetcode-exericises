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


#哈希表5 - 三数之和 (LeetCode 15):

#哈希表6 - 四数之和 (LeetCode 18):
