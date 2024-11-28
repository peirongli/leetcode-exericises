#2024-11-27
#贪心的本质是选择每一阶段的局部最优，从而达到全局最优。
#贪心算法一般分为如下四步：将问题分解为若干个子问题; 找出适合的贪心策略; 求解每一个子问题的最优解; 将局部最优解堆叠成全局最优解
#很多题也可以用动态规划做

#题1 - 分发饼干(leetcode 455)
#用大饼干先喂饱大胃口
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        g.sort()
        s.sort()
        idx = len(s) - 1
        
        for i in range(len(g)-1,-1,-1):
            if idx >= 0 and s[idx] >= g[i]: #注意要把idx>=0放在前面，否则会出现数组越界
                count += 1
                idx -= 1
        return count
#用小饼干先喂饱小胃口(没有第一种思路好理解)   
class Solution:
    def findContentChildren(self, g, s):
        g.sort()  
        s.sort()
        index = 0
        for i in range(len(s)):  # 遍历饼干
            if index < len(g) and g[index] <= s[i]:  # 如果当前孩子的贪心因子小于等于当前饼干尺寸
                index += 1  # 满足一个孩子，指向下一个孩子
        return index

#题2 - 摆动序列(leetcode 376)
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:  
        n = len(nums)
        if n < 2:
            return n
        elif n == 2:
            if nums[0] != nums[1]:
                return 2
            else:
                return 1
        else: #n >= 3
            preDiff,curDiff ,result  = 0, 0, 1
            for i in range(n-1):
                curDiff = nums[i + 1] - nums[i]
                if curDiff * preDiff <= 0 and curDiff !=0:  #差值为0时，不算摆动
                    result += 1
                    preDiff = curDiff
            return result

#题3 - 最大子序和(leetcode 53)
#局部最优：当前“连续和”为负数的时候立刻放弃，从下一个元素重新计算“连续和”，因为负数加上下一个元素 “连续和”只会越来越小。
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        result = float('-inf')
        curr_sum = 0
        for i in range(n):
            curr_sum += nums[i]
            if curr_sum > result:
                result = curr_sum
            if curr_sum < 0:
                curr_sum = 0     
        return result

#题4 - 买卖股票的最佳时机2(leetcode 122)
#代码不难, 主要是要想清楚
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        for i in range(1, n):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                profit += diff
        return profit

#题5 - 跳跃游戏(leetcode 55)
#每次取最大跳跃步数（取最大覆盖范围），整体最优解：最后得到整体最大覆盖范围，看是否能到终点。

#题6 - 跳跃游戏2(leetcode 45)

#题7 - k次取反后最大化的数组和(leetcode 1005)

#题8 - 加油站(leetcode 134)

#题9 - 分发糖果(leetcode 135)

#题10 - 柠檬水找零(leetcode 860)

#题11 - 根据身高重建队列(leetcode 406)

#题12 - 用最少数量的箭引爆气球(leetcode 452)

#题13 - 无重叠区间(leetcode 435)

#题14 - 划分字母区间(leetcode 763)

#题15 - 合并区间(leetcode 56)

#题16 - 单调自增的数字(leetcode 738)

#题17 - 监控二叉树(leetcode 968)

