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

#题8 - 复原IP地址(leetcode 93)

#part3 子集
#题9 - 子集(leetcode 78)

#题10 - 子集2(leetcode 90)

#题11 - 递增子序列(leetcode 491)

#part4 排列
#题12 - 全排列(leetcode 46)

#题13 - 全排列2(leetcode 47)

#part5 棋盘问题
#题14 - N皇后(leetcode 51)

#题15 - 解数独(leetcode 37)

#part6 其他
#题16 - 重新安排行程(leetcode 332)

