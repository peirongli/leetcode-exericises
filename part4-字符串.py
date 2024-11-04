#2024-11-3
#题1 - 反转字符串(leetcode 344)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        t = n // 2
        for i in range(t):
            temp = s[i]
            s[i] = s[n-1-i]
            s[n-1-i] = temp

#题2 - 反转字符串2(leetcode 541)
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        li = list(s)
        curr = 0 #current index
        total = len(s) #remaining unvisited
        n = len(s)
        while total >= 2*k:
            t = k // 2
            for j in range(t):
                temp = li[curr+j]
                li[curr+j] = li[curr+k-1-j]
                li[curr+k-1-j] = temp
            curr += 2*k
            total -= 2*k
        if total < k:
            t = total // 2
            for j in range(t):
                temp = li[curr+j]
                li[curr+j] = li[n-1-j]
                li[n-1-j] = temp
        if total < 2*k and total >= k:
            t = k // 2
            for j in range(t):
                temp = li[curr+j]
                li[curr+j] = li[curr+k-1-j]
                li[curr+k-1-j] = temp
        result = ''.join(li)
        return result

#题3 - 反转字符串中的单词(leetcode 151)
#空间复杂度O(n)解法(简单):
class Solution:
    def reverseWords(self, s: str) -> str:
        li = s.split()
        n = len(li)
        t = n // 2
        for i in range(t):
            temp = li[i]
            li[i] = li[n-1-i]
            li[n-1-i] = temp
        result = ' '.join(li)
        return result
#空间复杂度O(1)解法? To do

#题4 - 重复的子字符串(leetcode 459)
#初版: 暴力解法超时(通过74/129个测试用例)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                sub_str = s[i:j+1]
                sub_len = j-i+1
                if n % sub_len == 0:
                    t = n // sub_len
                    if t > 1 and sub_str * t == s:
                        return True
        return False
#改进暴力版: 符合条件的substring肯定包含第一个字符, 往后遍历到中间就行
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n <= 1:
            return False
        
        substr = ""
        for i in range(1, n//2 + 1):
            if n % i == 0:
                substr = s[:i]
                if substr * (n//i) == s:
                    return True
                
        return False
#进阶版: 移动匹配 - 判断 s + s 拼接的字符串里是否能出现一个s(要刨除s + s的首字符和尾字符)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n <= 1:
            return False
        ss = s[1:] + s[:-1] 
        print(ss.find(s))              
        return ss.find(s) != -1
#KMP算法
#主要思想: 当出现字符串不匹配时，可以知道一部分之前已经匹配的文本内容，从而利用这些信息避免从头再去做匹配
#如何记录: 前缀表 - 记录下标i之前（包括i）的字符串中，有多大长度的相同前缀与后缀
#针对本题: 如果一个字符串s是由重复子串组成，那么最长相等前后缀不包含的子串一定是字符串s的最小重复子串。
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:  
        if len(s) == 0:
            return False
        nxt = [0] * len(s)
        self.getNext(nxt, s)
        if nxt[-1] != 0 and len(s) % (len(s) - nxt[-1]) == 0:
            return True
        return False
    
    def getNext(self, nxt, s):
        nxt[0] = 0
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = nxt[j - 1]
            if s[i] == s[j]:
                j += 1
            nxt[i] = j
        return nxt
