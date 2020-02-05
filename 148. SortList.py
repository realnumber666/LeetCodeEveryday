# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #     def sortList(self, h: ListNode) -> ListNode:
    #         if h is None or h.next is None:
    #             return h
    #         pre = None
    #         slow = h
    #         fast = h

    #         while fast and fast.next:
    #             pre = slow
    #             slow = slow.next
    #             fast = fast.next.next
    #         pre.next = None # 断开链表为两个
    #         return self.mergeList(self.sortList(h), self.sortList(slow))

    #     def mergeList(self, l, r):
    #         if l is None:
    #             return r
    #         if r is None:
    #             return l
    #         if l.val <= r.val:
    #             l.next = self.mergeList(l.next, r)
    #             return l
    #         else:
    #             r.next = self.mergeList(l, r.next)
    #             return r
    def sortList(self, h: ListNode) -> ListNode:
        l = []
        node = h
        while node:
            l.append(node.val)
            node = node.next
        l.sort()
        node = h
        for n in l:
            node.val = n
            node = node.next
        return h