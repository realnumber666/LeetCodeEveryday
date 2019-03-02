#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (35.66%)
# Total Accepted:    519K
# Total Submissions: 1.4M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# 
# Input: "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: "{[]}"
# Output: true
# 
# 
#
class Solution:
    def isValid(self, s: str) -> bool:
        # 栈，如果一个进入时，若为右括号，进行匹配，则弹出栈尾;不匹配，则入栈
                            # 若不为右括号，直接入站
        # 流程结束后，栈未空，则false
        stack = []
        if(len(s) == 0):
            return True
        if(len(s) == 1 or len(s) % 2 != 0):
            return False
        for c in s:
            if(len(stack) != 0):
                if(c == ')'):
                    if(stack[-1] == '('):
                        stack.pop()
                        continue
                elif(c == '}'):
                    if(stack[-1] == '{'):
                        stack.pop()
                        continue
                elif(c == ']'):
                    if(stack[-1] == '['):
                        stack.pop()
                        continue
            stack.append(c)
        if(len(stack) == 0):
            return True
        else:
            return False
        '''
        1. 先把特殊情况处理掉，比如0，1，奇数偶数
        2. 一定要看清题干，会不会是空的，如果是空的算true or false
        3. 多给自己测几个用例
        '''        

