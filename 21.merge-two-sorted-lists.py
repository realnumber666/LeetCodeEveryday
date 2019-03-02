#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (45.31%)
# Total Accepted:    513.1K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        两个指针分别指l1，l2的头
        新建一个listnode
        比较俩指针的值，小的那个连上新队列，该指针往后走
            连新队列的方法：val赋值；新建node；指针跳到下一个node
        直到两个指针都指着none结束
        '''
        head = ListNode(0)
        ptr =  head
        ptr1 = l1
        ptr2 = l2
        if(ptr1 == None or ptr2 == None):
            return ptr1 if ptr2 == None else ptr2
        while(ptr1 or ptr2):
            if(ptr1 == None):
                ptr.val = ptr2.val
                ptr.next = ptr2.next if ptr2.next else None
                return head
            if(ptr2 == None):
                ptr.val = ptr1.val
                ptr.next = ptr1.next if ptr1.next else None
                return head
            if(ptr1.val <= ptr2.val):
                value = ptr1.val
                ptr1 = ptr1.next
            else:
                value = ptr2.val
                ptr2 = ptr2.next
            print(value, ptr1, ptr2)
            ptr.val = value
            ptr.next = ListNode(0)
            ptr = ptr.next
        return head
        '''
        1. 链表一定要记得判断next到底有没有东西，到底什么时候结束流程
        '''        

