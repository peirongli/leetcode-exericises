#2025-02
#一、基础问题
#题1: 斐波那契数列(leetcode 509)
#虽然简单, 但要注意一下下标细节
class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        f = [0]*(n+1)
        f[0] = 0
        f[1] = 1
        for i in range(2, n+1):
            f[i] = f[i-1] +f[i-2]
        return f[n]

#题2: 爬楼梯(leetcode 70)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        ways = [0]*(n+1)
        ways[1] = 1
        ways[2] = 2
        for i in range(3, n+1):
            ways[i] = ways[i-2] + ways[i-1]
        return ways[n]

#题3: 使用最小花费爬楼梯(leetcode 746)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        #if n == 0 or n == 1:
            #return 0
        minCost = [inf] * (n+1)
        minCost[0] = 0
        minCost[1] = 0
        for i in range(2, n+1):
            minCost[i] = min(minCost[i-1]+cost[i-1], minCost[i-2]+cost[i-2])
        return minCost[n]

#题4: 不同路径(leetcode 62)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ways = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            ways[i][0] = 0
        for i in range(n+1):
            ways[0][i] = 0
        ways[1][1] = 1
        #ways[1][2] = 1
        #ways[2][1] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 and j == 1:
                    continue
                ways[i][j] = ways[i-1][j] + ways[i][j-1]

        return ways[m][n]

#题5: 不同路径II(leetcode 63)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0]) if obstacleGrid else 0
        ways = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            ways[i][0] = 0
        for i in range(n+1):
            ways[0][i] = 0
        ways[1][1] = 1

        if obstacleGrid[0][0] == 1: #case37, 注意下特殊情况(障碍在起点)
            return 0 

        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 and j == 1:
                    continue
                if obstacleGrid[i-1][j-1] == 1:
                    ways[i][j] = 0
                else:
                    ways[i][j] = ways[i-1][j] + ways[i][j-1]

        return ways[m][n]

#题6: 整数拆分(leetcode 343)

#题7: 不同的二叉搜索树(leetcode 96)

#二、背包问题
#2.1: 0-1背包

#题8: 分割等和子集(leetcode 416)

#题9: 最后一块石头的重量2(leetcode 1049)

#题10: 目标和(leetcode 494)

#题11: 一和零(leetcode 474)

#2.2: 完全背包

#题12: 零钱兑换(leetcode 322)

#题13: 零钱兑换II(leetcode 518)

#题14: 组合总和IV(leetcode 377)

#题15: 完全平方数(leetcode 279)

#题16: 单词拆分(leetcode 139)

#三、打家劫舍
#题17: 打家劫舍(leetcode 198)

#题18: 打家劫舍II(leetcode 213)

#题19: 打家劫舍III(leetcode 337)

#四、股票问题
#题20: 买卖股票的最佳时机(leetcode 121)

#题21: 买卖股票的最佳时机II(leetcode 122)

#题22: 买卖股票的最佳时机III(leetcode 123)

#题23: 买卖股票的最佳时机IV(leetcode 188)

#题24: 买卖股票的最佳时机含手续费(leetcode 714)

#题25: 最佳买卖股票时机含冷冻期(leetcode 309)

#五、子序列问题
#题26: 最长递增子序列(leetcode 300)

#题27: 最长连续递增序列(leetcode 674)

#题28: 最长重复子数组(leetcode 718)

#题29: 最长公共子序列(leetcode 1143)

#题30: 不相交的线(leetcode 1035)

#题31: 最大子序和(leetcode 53)

#题32: 判断子序列(leetcode 392)

#题33: 不同的子序列(leetcode 115)

#题34: 两个字符串的删除操作(leetcode 583)

#题35: 编辑距离(leetcode 72)

#题36: 回文子串(leetcode 647)

#题37: 最长回文子序列(leetcode 516)
