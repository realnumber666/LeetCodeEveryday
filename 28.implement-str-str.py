#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr/description/
#
# algorithms
# Easy (31.01%)
# Total Accepted:    383.7K
# Total Submissions: 1.2M
# Testcase Example:  '"hello"\n"ll"'
#
# Implement strStr().
# 
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
# 
# Example 1:
# 
# 
# Input: haystack = "hello", needle = "ll"
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# 
# 
# Clarification:
# 
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
# 
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
# 
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        获得needle的length，字符串转数组，
        while i+ne_len<=hay_len:i=0，连着length位进行比较，若匹配，return i
                                         若不匹配，i自增，
        return -1
        ---
        needle空，0
        haystack空，-1
        haystack < needle,-1
        '''
        ne_len = len(needle)
        hay_len = len(haystack)
        # haystack = list(haystack)
        i = 0
        if(ne_len == 0): return 0
        if(hay_len == 0): return -1
        if(hay_len < ne_len): return -1
        if(hay_len == ne_len):
            if(haystack[i:ne_len] == needle):
                return 0
            else: return -1
        while(i + ne_len <= hay_len):
            print(haystack[i:i+ne_len], needle)
            if(haystack[i:i+ne_len] == needle):
                return i
            else:
                i += 1
        return -1
        '''
        1. 保持这个思路和状态
        2. 有些没必要的比较提前跳出，比如第一个匹配成功，第二个没匹配成功，就直接跳出，而不是用[::]来比较
        '''      

