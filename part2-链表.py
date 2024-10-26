#2024-10-26
# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None): #val有时候需要定义默认值, 有时候不需要
        self.val = val
        self.next = next

#链表1 - 移除链表元素 (leetcode 203):
#方法一: 对头节点单独处理
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #如果头节点就是要删除的, 做特殊处理
        while(head != None and head.val == val):
            head = head.next

        curr = head
        while(curr != None and curr.next != None):
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head
#方法二: 增加一个虚拟头节点
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 创建虚拟头节点
        dummy_head = ListNode(next = head)
        
        current = dummy_head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy_head.next #注意不是直接return head

#链表2 - 设计链表 (leetcode 707):
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        else:
            curr = self.dummy_head.next
            for i in range(index):
                curr = curr.next
            return curr.val

    def addAtHead(self, val: int) -> None:
        self.dummy_head.next = ListNode(val, self.dummy_head.next)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        curr = self.dummy_head
        while curr.next: #这里用while比用for循环好
            curr = curr.next

        curr.next = ListNode(val, None)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size: #注意这里是>size而不是>=, =时效果和addAtTail一样
            return
        
        curr = self.dummy_head
        for i in range(index):
            curr = curr.next
        curr.next = ListNode(val, curr.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        curr = self.dummy_head
        for i in range(index):
            curr = curr.next

        curr.next = curr.next.next
        self.size -= 1

#链表3 - 反转链表 (leetcode 206):
#双指针(用递归也行)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        curr = head
        while(curr != None):
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
        return pre

#链表4 - 两两交换链表中的节点 (leetcode 24):
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next = head)
        curr = dummy_head
        while (curr.next and curr.next.next):
            temp1 = curr.next
            temp2 = curr.next.next
            temp3 = curr.next.next.next

            curr.next = temp2
            curr.next.next = temp1
            temp1.next = temp3

            curr = curr.next.next
        return dummy_head.next

#链表5 - 删除链表的倒数第 N 个结点 (leetcode 19):

#链表6 - 环形链表2 (leetcode 142):
