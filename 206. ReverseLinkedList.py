# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        l m r 三个指针
        m指向l,l = m, m = r, r = r.next
        直到r.next = None
        '''
        # []
        if head is None:
            return None

        l = head
        # [1]
        if l.next is None:
            return l

        # [1, 2]
        m = l.next
        r = m.next
        l.next = None  # 不然会出现循环链表

        while r != None:
            m.next = l
            l = m
            m = r
            r = r.next

        m.next = l

        return m