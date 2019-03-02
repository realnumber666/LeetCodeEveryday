#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (32.84%)
# Total Accepted:    411.4K
# Total Submissions: 1.2M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# 
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 第i轮遍历每个str的第i个字符，若有不同立即退出，这个字符不算
        # 每一轮遍历开始存下第一个字符
        res = []
        i = 0
        if(len(strs) == 0): return ''
        while i < len(strs[0]):
            flag = 1
            c = strs[0][i]
            for s in strs:
                if(i >= len(s) or s[i] != c):
                    flag = 0
                    break
            if(flag == 0):
                break
            res.append(c)
            i += 1
        return ''.join(res)
        '''
        1. 应该第一步理清的思路是，那个循环在外，那个循环在内
        2. 下标从零开始，不能再写错啦！
        3. 还是有边界条件没考虑到，写代码之前，第一步理思路，第二步思考边界条件
        4* 用一个flag来帮助跳出多层循环
        '''

