#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (41.41%)
# Total Accepted:    513.6K
# Total Submissions: 1.2M
# Testcase Example:  '121'
#
# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backward as forward.
# 
# Example 1:
# 
# 
# Input: 121
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
# 
# 
# Example 3:
# 
# 
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# 
# 
# Follow up:
# 
# Coud you solve it without converting the integer to a string?
# 
#
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Solution1 弟弟行为
        # return str(x) == str(x)[::-1]
        # Solution2 哥哥行为
        if(x < 0):
            return False
        str_x = str(x)
        if(len(str_x) < 2  or (len(str_x) == 2 and x % 11 == 0)):
            return True        
        mid = int(len(str_x)/2)
        i = 0
        while i < mid:
            if(str_x[i] != str_x[len(str_x) - 1 - i]):
                return False
            i += 1
        return True
        

