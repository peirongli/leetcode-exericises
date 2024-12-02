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
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        cover = 0
        for i in range(n):
            if i <= cover: #注意
                cover = max(i + nums[i], cover)
                if cover >= n - 1:
                    return True
        return False

#题6 - 跳跃游戏2(leetcode 45)
#以最小的步数增加最大的覆盖范围，直到覆盖范围覆盖了终点

#题7 - k次取反后最大化的数组和(leetcode 1005)
#思路不难, 但有一些小细节需要处理好
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        #max_sum = 0
        count_neg, count_zero, count_pos = 0, 0, 0
        for i in range(n):
            if nums[i] > 0:
                count_pos += 1
            elif nums[i] < 0:
                count_neg += 1
            else:
                count_zero += 1
        if k <= count_neg:
            for i in range(k):
                nums[i] = -nums[i]
            
        elif k > count_neg:
            for i in range(count_neg):
                nums[i] = -nums[i]
            rest = k - count_neg
            if count_zero == 0 and rest%2 == 1:
                if count_pos != 0:
                    if abs(nums[count_neg]) < abs(nums[count_neg-1]):
                        nums[count_neg] = -nums[count_neg]
                    else:
                        nums[count_neg-1] = -nums[count_neg-1]
                else:
                    nums[count_neg-1] = -nums[count_neg-1]

        max_sum = sum(nums)
        return max_sum

#题8 - 加油站(leetcode 134)
#暴力法 O(n^2) (超时, 通过34/39个测试用例)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            curr_gas = 0
            j = 0
            while j < n:             
                curr_gas = curr_gas + gas[(i+j)%n] - cost[(i+j)%n]
                if curr_gas < 0:
                    break
                j += 1
            if curr_gas >= 0:
                return i
        return -1
#贪心1:
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curSum = 0  # 当前累计的剩余油量
        minFuel = float('inf')  # 从起点出发，油箱里的油量最小值
        
        for i in range(len(gas)):
            rest = gas[i] - cost[i]
            curSum += rest
            if curSum < minFuel:
                minFuel = curSum
        
        if curSum < 0:
            return -1  # 情况1：整个行程的总消耗大于总供给，无法完成一圈
        
        if minFuel >= 0:
            return 0  # 情况2：从起点出发到任何一个加油站时油箱的剩余油量都不会小于0，可以从起点出发完成一圈
        
        for i in range(len(gas) - 1, -1, -1):
            rest = gas[i] - cost[i]
            minFuel += rest
            if minFuel >= 0:
                return i  # 情况3：找到一个位置使得从该位置出发油箱的剩余油量不会小于0，返回该位置的索引
        
        return -1
#贪心2:
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curSum = 0  # 当前累计的剩余油量
        totalSum = 0  # 总剩余油量
        start = 0  # 起始位置
        
        for i in range(len(gas)):
            curSum += gas[i] - cost[i]
            totalSum += gas[i] - cost[i]
            
            if curSum < 0:  # 当前累计剩余油量curSum小于0
                start = i + 1  # 起始位置更新为i+1
                curSum = 0  # curSum重新从0开始累计
        
        if totalSum < 0:
            return -1  # 总剩余油量totalSum小于0，说明无法环绕一圈
        return start
    
#题9 - 分发糖果(leetcode 135)
#要分两遍遍历: 先确定右边评分大于左边的情况（也就是从前向后遍历), 再确定左边评分大于右边的情况（也就是从后向前遍历）
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        nums = [1]*n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                nums[i] = nums[i-1] + 1
        for i in range(n-2,-1,-1):
             if ratings[i] > ratings[i + 1] and nums[i] <= nums[i+1]:
                nums[i] = nums[i+1] + 1
            
        result = sum(nums)
        return result

#题10 - 柠檬水找零(leetcode 860)
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash_5, cash_10, cash_20 = 0, 0, 0
        n = len(bills)
        for i in range(n):
            if bills[i] == 5:
                cash_5 += 1
            elif bills[i] == 10:
                cash_10 += 1
                if cash_5 < 1:
                    return False
                cash_5 -= 1       
            else: #bill[i] == 20
                cash_20 += 1       
                if cash_10 < 1 and cash_5 < 3:
                    return False
                elif cash_10 >= 1 and cash_5 < 1:
                    return False
                elif cash_10 >= 1 and cash_5 >= 1: #way1: 10+5
                    cash_10 -= 1
                    cash_5 -= 1
                else: #way2: 5+5+5
                    cash_5 -= 3
        return True

#题11 - 根据身高重建队列(leetcode 406)
#代码看着简单, 但要思考的比较多
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        queue = []
        n = len(people)
        people.sort(key=lambda x: (-x[0], x[1])) # lambda返回的是一个元组：当-x[0](维度h）相同时，再根据x[1]（维度k）从小到大排序
        for p in people:
            queue.insert(p[1], p)
        return queue
    
#题12 - 用最少数量的箭引爆气球(leetcode 452)
#自己写的逻辑错误版(通过24/50个测试用例):
class Solution:
    def findMinArrowShots(self, points):
        n = len(points)
        count = n
        overlap = 0
        points.sort(key=lambda x: (x[0], x[1]))
        
        i = 0
        visited = 1
        while i < n:
            for j in range(i+1, n):
                if visited >= n:
                    return count - overlap
                if points[i][1] >= points[j][0]:
                    overlap += 1
                    visited += 1
                else:
                    i = j - 1
                    break
            i += 1
            visited += 1
                
        count -= overlap
        return count
#正确版:
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        points.sort(key=lambda x: x[0])
        result = 1
        for i in range(1, len(points)):
            if points[i][0] > points[i - 1][1]: # 气球i和气球i-1不挨着，注意这里不是>=
                result += 1     
            else:
                points[i][1] = min(points[i - 1][1], points[i][1]) # 更新重叠气球最小右边界
        return result

#题13 - 无重叠区间(leetcode 435)
#在上一题的基础上稍作修改即可
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key = lambda x: (x[0], x[1]))

        result = 1
        for i in range(1, n):
            if intervals[i][0] >= intervals[i - 1][1]:
                result += 1     
            else:
                intervals[i][1] = min(intervals[i - 1][1], intervals[i][1])
        count = n - result
        return count

#题14 - 划分字母区间(leetcode 763)

#题15 - 合并区间(leetcode 56)

#题16 - 单调自增的数字(leetcode 738)

#题17 - 监控二叉树(leetcode 968)

