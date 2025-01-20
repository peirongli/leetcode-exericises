#2025-1
#part1 组合
#题1 - 组合(leetcode 77)
class Solution:
    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:]) #注意这里要用path[:]而不是path，否则result里面的元素会随着path的改变而改变
            return
        for i in range(startIndex, n + 1):
            path.append(i)
            self.backtracking(n, k, i + 1, path, result)
            path.pop()
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.backtracking(n, k, 1, [], result)
        return result
#题2 - 组合(优化版)
class Solution:
    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(startIndex, n - (k - len(path)) + 2):  #优化的地方
            path.append(i)
            self.backtracking(n, k, i + 1, path, result)
            path.pop()
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.backtracking(n, k, 1, [], result)
        return result

#题3 - 组合总和3(leetcode 216)
#不剪枝会超时:
class Solution:
    def backtracking(self, n, k, startIdx, path, result):
        if len(path) == k and sum(path) == n:
            result.append(path[:])
            return result
        for i in range(startIdx, n + 1):
            path.append(i)
            self.backtracking(n, k, i + 1, path, result)
            path.pop()
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.backtracking(n, k, 1, [], result)
        return result
#剪枝后:
class Solution:
    def backtrack(self, n, k, start, path, result):
        if sum(path) > n: #剪枝
            return
        if sum(path) == n and len(path) == k:
            result.append(path[:])
            return
        for i in range(start, 10):
            path.append(i)
            self.backtrack(n, k, i+1, path, result)
            path.pop()
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.backtrack(n, k, 1, [], result)
        return result

#题4 - 电话号码的字母组合(leetcode 17)
#虽然没完全懂但是套模版做出来了
#横向遍历-for循环, 纵向遍历-for循环内的递归
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numbers = list(digits)
        pairs = {}
        if "2" in numbers:
            pairs.update({"2":["a","b","c"]})
        if "3" in numbers:
            pairs.update({"3":["d","e","f"]})
        if "4" in numbers:
            pairs.update({"4":["g","h","i"]})
        if "5" in numbers:
            pairs.update({"5":["j","k","l"]})
        if "6" in numbers:
            pairs.update({"6":["m","n","o"]})
        if "7" in numbers:
            pairs.update({"7":["p","q","r","s"]})
        if "8" in numbers:
            pairs.update({"8":["t","u","v"]})
        if "9" in numbers:
            pairs.update({"9":["w","x","y","z"]})
        
        n = len(numbers)
        if n == 0:
            return []
        if n == 1:
            result = pairs[digits]
        else:
            result = [] 
            self.backtrack(n, 0, numbers, pairs, [], result)
        return result
    def backtrack(self, n, idx, numbers, pairs, path, result):
        if len(path) == n:
            temp = ''.join(path)
            result.append(temp)
            return
        curr = numbers[idx]
        vals = pairs[curr]
        l = len(vals)
        for i in range(l):
            path.append(vals[i])
            self.backtrack(n, idx+1, numbers, pairs, path, result)
            path.pop()

#题5 - 组合总和(leetcode 39)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        result = []
        self.backtrack(candidates, n, target, 0, [], result)
        return result
    def backtrack(self, candidates, n, target, start, path, result):
        if sum(path) > target:
            return
        if sum(path) == target:
            result.append(path[:])
            return
        for i in range(start, n):
            path.append(candidates[i])
            self.backtrack(candidates, n, target, i, path, result)
            path.pop()

#题6 - 组合总和2(leetcode 40)
#最初的想法(在1的基础上稍微修改): 错误, 会有重复的组合
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        result = []
        self.backtrack(candidates, n, target, 0, [], result)
        return result
    def backtrack(self, candidates, n, target, start, path, result):
        if sum(path) > target:
            return
        if sum(path) == target:
            result.append(path[:])
            return
        for i in range(start, n):
            path.append(candidates[i])
            self.backtrack(candidates, n, target, i+1, path, result)
            path.pop()
#如何去重: 用used数组
class Solution:
    def backtracking(self, candidates, target, total, startIndex, used, path, result):
        if total == target:
            result.append(path[:])
            return

        for i in range(startIndex, len(candidates)):
            # 对于相同的数字，只选择第一个未被使用的数字，跳过其他相同数字
            if i > startIndex and candidates[i] == candidates[i - 1] and not used[i - 1]:
                continue

            if total + candidates[i] > target:
                break

            total += candidates[i]
            path.append(candidates[i])
            used[i] = True
            self.backtracking(candidates, target, total, i + 1, used, path, result)
            used[i] = False
            total -= candidates[i]
            path.pop()

    def combinationSum2(self, candidates, target):
        used = [False] * len(candidates)
        result = []
        candidates.sort()
        self.backtracking(candidates, target, 0, 0, used, [], result)
        return result

#part2 分割
#题7 - 分割回文串(leetcode 131)
#思路不难理解, 实际细节有点复杂
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.backtracking(s, 0, [], result)
        return result

    def backtracking(self, s, start_index, path, result):
        if start_index == len(s):
            result.append(path[:])
            return
        
        for i in range(start_index, len(s)):
            if self.is_palindrome(s, start_index, i):
                path.append(s[start_index:i+1])
                self.backtracking(s, i+1, path, result)
                path.pop()

    def is_palindrome(self, s: str, start: int, end: int) -> bool:#用双指针的好处: 不用每次都切片处理
        i: int = start        
        j: int = end
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

#题8 - 复原IP地址(leetcode 93)
#改一下上题的判断函数就行, 本质一样
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        self.backtracking(s, 0, [], result)
        return result

    def backtracking(self, s, start_index, path, result):
        if len(path) > 4:
            return
        if start_index == len(s) and len(path) == 4:
            temp_addr = '.'.join(path)
            result.append(temp_addr)
            return
        
        for i in range(start_index, len(s)):
            if self.isVaild(s, start_index, i):
                path.append(s[start_index:i+1])
                self.backtracking(s, i+1, path, result)
                path.pop()

    def isVaild(self, s: str, start: int, end: int) -> bool:
        temp_str = s[start:end+1]
        if s[start] == '0' and len(temp_str) > 1:
            return False
        if int(temp_str) < 0 or int(temp_str) > 255:
            return False
        return True

#part3 子集
#题9 - 子集(leetcode 78)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(nums, 0, [], result)
        return result
    def backtrack(self, nums, start, path, result):
        #不需要终止条件
        result.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            self.backtrack(nums, i+1, path, result)
            path.pop()

#题10 - 子集2(leetcode 90)
#按常规的想法应该要用used数组去重, 但貌似排序之后再加一行判断也行?
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        self.backtrack(nums, 0, [], result)
        return result
    def backtrack(self, nums, start, path, result):
        temp = path[:]
        if temp not in result:
            result.append(temp)

        for i in range(start, len(nums)):
            path.append(nums[i])
            self.backtrack(nums, i+1, path, result)
            path.pop()

#题11 - 递增子序列(leetcode 491)
#笨方法, 很极限没超时
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(nums, 0, [], result)
        return result

    def backtrack(self, nums, start, path, result):
        if len(path) > 1 and self.isAscending(path):
            temp = path[:]
            if temp not in result:
                result.append(temp)

        for i in range(start, len(nums)):
            path.append(nums[i])
            self.backtrack(nums, i+1, path, result)
            path.pop()
            
    def isAscending(self, numbers):
        for i in range(len(numbers)-1):
            if numbers[i+1] < numbers[i]:
                return False
        return True
#set去重:
class Solution:
    def findSubsequences(self, nums):
        result = []
        self.backtracking(nums, 0, [], result)
        return result
    
    def backtracking(self, nums, startIndex, path, result):
        if len(path) > 1:
            result.append(path[:])
            # 注意这里不要加return，要取树上的节点
        
        uset = set()  # 使用集合对本层元素进行去重
        for i in range(startIndex, len(nums)):
            if (path and nums[i] < path[-1]) or nums[i] in uset:
                continue
            
            uset.add(nums[i])  # 记录这个元素在本层用过了，本层后面不能再用了
            path.append(nums[i])
            self.backtracking(nums, i + 1, path, result)
            path.pop()

#part4 排列
#题12 - 全排列(leetcode 46)

#题13 - 全排列2(leetcode 47)

#part5 棋盘问题
#题14 - N皇后(leetcode 51)

#题15 - 解数独(leetcode 37)

#part6 其他
#题16 - 重新安排行程(leetcode 332)

