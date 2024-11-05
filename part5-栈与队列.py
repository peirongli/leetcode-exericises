#2024-11-5
#题1 - 用栈实现队列(leetcode 232)
class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self) -> int:
        ans = self.pop()
        self.stack_out.append(ans)
        return ans
    
    def empty(self) -> bool:
        return not (self.stack_in or self.stack_out)
    
#题2 - 用队列实现栈(leetcode 225)
#用一个双向队列
from collections import deque
class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        n = len(self.queue)
        for i in range(n-1):
            self.queue.append(self.queue.popleft())
        return self.queue.popleft()

    def top(self) -> int:
        if self.empty():
            return None
        n = len(self.queue)
        for i in range(n-1):
            self.queue.append(self.queue.popleft())
        temp = self.queue.popleft()
        self.queue.append(temp)
        return temp

    def empty(self) -> bool:
        return not self.queue
#用两个队列
from collections import deque
class MyStack:
    def __init__(self):
        """
        in - 存所有数据
        out - 仅在pop的时候会用到
        """
        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, x: int) -> None:
        self.queue_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None

        for i in range(len(self.queue_in) - 1):
            self.queue_out.append(self.queue_in.popleft())
        
        self.queue_in, self.queue_out = self.queue_out, self.queue_in    # 交换in和out，这也是为啥in只用来存
        return self.queue_out.popleft()

    def top(self) -> int:
        # 写法一：
        # if self.empty():
        #     return None
        
        # return self.queue_in[-1]    # 这里实际上用到了栈，因为直接获取了queue_in的末尾元素

        # 写法二：
        if self.empty():
            return None

        for i in range(len(self.queue_in) - 1):
            self.queue_out.append(self.queue_in.popleft())
        
        self.queue_in, self.queue_out = self.queue_out, self.queue_in 
        temp = self.queue_out.popleft()   
        self.queue_in.append(temp)
        return temp

    def empty(self) -> bool:
        return len(self.queue_in) == 0

#题3 - 有效的括号(leetcode 20)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '{':
                stack.append('}')
            elif char == '[':
                stack.append(']')
            elif not stack or stack[-1] != char:
                return False
            else:
                stack.pop()
        if not stack:
            return True
        else:
            return False

#题4 - 删除字符串中的所有相邻重复项(leetcode 1047)
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if not stack:
                stack.append(char)          
            elif char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
                
        result = ''.join(stack)
        return result

#题5 - 逆波兰表达式求值(leetcode 150)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for element in tokens:
            if element == '+':
                temp2 = int(stack.pop())
                temp1 = int(stack.pop())
                res = temp1 + temp2
                stack.append(str(res))
            elif element == '-':
                temp2 = int(stack.pop())
                temp1 = int(stack.pop())
                res = temp1 - temp2
                stack.append(str(res))
            elif element == '*':
                temp2 = int(stack.pop())
                temp1 = int(stack.pop())
                res = temp1 * temp2
                stack.append(str(res))
            elif element == '/':
                temp2 = int(stack.pop())
                temp1 = int(stack.pop())
                res = temp1 // temp2
                if temp1 % temp2 != 0 and res < 0:
                    res += 1
                stack.append(str(res))
            else:
                stack.append(element)
        if len(stack) != 1:
            return None
        else:
            result = int(stack[0])
            return result

#题6 - 滑动窗口最大值(leetcode 239)
#暴力法: 时间复杂度O(nk), 会超时(通过37/51个测试用例)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n-k+1):
            temp = nums[i: i + k]
            res = max(temp)
            result.append(res)
        return result
#单调队列, 时间复杂度O(n)

#题7 - 前K个高频元素(leetcode 347)
