#2024-10-24
#数组1 - 二分法 (leetcode 704):
#使用前提: 有序数组且无重复元素
class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while(left <= right): #这里选用左闭右闭写法, 即while里面用left <= right
            mid  =(left + right) // 2 #可以写作mid = left + (right - left) // 2 来防止溢出
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        return -1

#数组2 - 移除元素 (leetcode 27):
#限制条件: 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间, 并原地修改输入数组。
#解法一: 暴力双循环 时间复杂度O(n^2)
class Solution:
    def remove(self, nums, val):
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == val:
                for j in range(i, n-1):
                    nums[j] = nums[j+1] #数组整体向前移一位来覆盖目标值
                n = n - 1 #理论上的数组的长度-1 (实际上没变)
                i = i - 1 #因为下标i以后的数值都向前移动了一位，所以i也向前移动一位
            i = i + 1
        return n
#解法二: 双指针法 时间复杂度O(n)
#快指针: 寻找新数组(不含有目标元素的数组)的元素
#慢指针: 指向更新 新数组下标的位置
class Solution:
    def remove(self, nums, val):
        n = len(nums)
        slow = 0
        for fast in range(n):
            if nums[fast] != val: #如果快指针指向的元素不等于目标值, 就把这个元素放到慢指针指向的位置; 如果等于目标值, 就跳过这个元素
                nums[slow] = nums[fast]
                slow = slow + 1
        return slow
    
#数组3 - 有序数组的平方 (leetcode 977):
#为了O(n)的时间复杂度, 需要使用双指针法
#trick: 因为数组是非递减的, 所以平方最大值只可能在头和尾, 所以只要从两头往中间缩小范围就行
class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        result = [float('inf')] * n #注意: 需要新建一个list存放结果, 不能直接在原list上操作
        left = 0
        right = n - 1
        i = n - 1
        while left <= right: #注意这里要left <= right，因为最后要处理两个元素
            if nums[left] * nums[left] < nums[right] * nums[right]:
                result[i] = nums[right] * nums[right]
                right -= 1
            else:
                result[i] = nums[left] * nums[left]
                left += 1
            i -= 1
        return result
    
#数组4 - 长度最小的子数组 (leetcode 209):
#滑动窗口(本质上还是双指针) 稍微有点难理解
#窗口的定义: 满足其中元素之和 ≥ s 的长度最小的连续子数组
#窗口的起始位置如何移动：如果当前窗口的值大于等于s了，窗口就要向前移动了（也就是该缩小了）。
#窗口的结束位置如何移动：窗口的结束位置就是遍历数组的指针，也就是for循环里的索引。
#trick: 在移动终止位置的时候，初始位置是不可逆的，初始位置只可能往后移动，而不用每次都从第零个元素开始
class Solution:
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        result = n + 1
        i = 0 #i为窗口起点
        sum = 0
        for j in range(n): #j为窗口终点
            sum += nums[j]
            while sum >= target:
                temp = j - i + 1
                result = min(result, temp)
                sum -= nums[i]
                i += 1 #移动窗口起点

        if result == n + 1:
            return 0
        else:
            return result
#注意: 虽然用了两层循环, 但时间复杂度仍然是O(n), 因为指针 start 和 end 最多各移动 n 次。

#数组5 - 螺旋矩阵2 (leetcode 59):

