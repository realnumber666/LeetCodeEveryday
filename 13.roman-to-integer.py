#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#
# https://leetcode.com/problems/roman-to-integer/description/
#
# algorithms
# Easy (51.25%)
# Total Accepted:    366.3K
# Total Submissions: 710.5K
# Testcase Example:  '"III"'
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D
# and M.
# 
# 
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 
# For example, two is written as II in Roman numeral, just two one's added
# together. Twelve is written as, XII, which is simply X + II. The number
# twenty seven is written as XXVII, which is XX + V + II.
# 
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is
# written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX. There
# are six instances where subtraction is used:
# 
# 
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# 
# 
# Given a roman numeral, convert it to an integer. Input is guaranteed to be
# within the range from 1 to 3999.
# 
# Example 1:
# 
# 
# Input: "III"
# Output: 3
# 
# Example 2:
# 
# 
# Input: "IV"
# Output: 4
# 
# Example 3:
# 
# 
# Input: "IX"
# Output: 9
# 
# Example 4:
# 
# 
# Input: "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# 
# 
# Example 5:
# 
# 
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
# 
#
class Solution:
    def romanToInt(self, s: str) -> int:
        # 三种特殊情况单列, 若碰到I X C进行判断，flag=i，下一次轮匹配，配上了删一个数字，加一个结果数字，没配上直接加原数字，flag=0
        # 初始化一个字典来匹配
        sym = {'I': 1, 'V':5, 'X': 10,'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        flag = None
        res = 0
        carry = 0
        for i in s:
            if flag:
                if(flag == 'I'):
                    if(i == 'V'):
                        carry = 4
                    elif(i == 'X'):
                        carry = 9
                elif(flag == 'X'):
                    if(i == 'L'):
                        carry = 40
                    elif(i == 'C'):
                        carry = 90
                elif(flag == 'C'):
                    if(i == 'D'):
                        carry = 400
                    elif(i == 'M'):
                        carry = 900                        
                if(carry != 0):
                    print(flag, sym[flag], carry)
                    res = res - sym[flag] + carry
                    carry = 0
                    print(res)
                    flag = None
                    continue
                else:
                    flag = None                
            if(i == 'I' or i == 'X' or i == 'C'):
                flag = i
            res += sym[i]
        return res

        

