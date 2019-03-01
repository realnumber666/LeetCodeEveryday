#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (30.35%)
# Total Accepted:    769.5K
# Total Submissions: 2.5M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        i = j = 0
        num1 = num2 = 0
        while l1 != None:
            num1 += int(l1.val) * pow(10, i)
            l1 = l1.next
            i += 1
        while l2 != None:
            num2 += int(l2.val) * pow(10, j)
            l2 = l2.next
            j += 1
        print(num1, num2)
        total = num1 + num2
        m = more1 = more2 = 0 # more2为本次，more1为上次
        l3 = ListNode(0)
        more2 = total % 10
        l3 = ListNode(0)
        ptr = l3
        print(total)
        flag = 0
        while flag != 1:
            m += 1
            if(more2 == total): 
                flag = 1
                ptr.val = int((more2 - more1)/pow(10, m - 1))
                break
            ptr.val = int((more2 - more1)/pow(10, m - 1))
            print(ptr.val)
            ptr.next = ListNode(0)
            ptr = ptr.next
            more1 = more2
            more2 = total % pow(10, m + 1)       
        return l3

