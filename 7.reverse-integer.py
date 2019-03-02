#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.05%)
# Total Accepted:    613.4K
# Total Submissions: 2.4M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
# this problem, assume that your function returns 0 when the reversed integer
# overflows.
# 
#
class Solution:
    def reverse(self, x: int) -> int:
        neg = 0
        if x == 0:
            return 0
        elif(x <= 0):
            x = -x
            neg = 1
        flag = m = more1 = more2 = 0
        arr = []
        more2 = x % pow(10, m + 1) # 0
        while True:            
            m += 1 # 1
            if flag == 1:
                break
            elif flag == 0 and more2 == x:
                flag = 1            
            arr.append(int((more2 - more1)/pow(10, m - 1)))
            more1 = more2
            more2 = x % pow(10, m + 1)
        lenth = len(arr)
        res = 0
        for i in range(lenth):
            res += arr[i]*pow(10, (lenth-i-1))
        if(neg == 1):
            res = -res
        if(res> (pow(2, 31) - 1) or res < (-pow(2, 31))):
            return 0
        return res
        

