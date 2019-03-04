#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say/description/
#
# algorithms
# Easy (39.18%)
# Total Accepted:    259.9K
# Total Submissions: 657.4K
# Testcase Example:  '1'
#
# The count-and-say sequence is the sequence of integers with the first five
# terms as following:
# 
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# 
# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the
# count-and-say sequence.
# 
# Note: Each term of the sequence of integers will be represented as a
# string.
# 
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: "1"
# 
# 
# Example 2:
# 
# 
# Input: 4
# Output: "1211"
# 
#
class Solution:
    def ifZero(self, first:int, n: int) -> str:
        if(first != 0 and n == 0):
            return '1'
        return str(n)
    def countAndSay(self, n: int) -> str:
        '''
        recursion
        没解到1就一直递归
        对上一层迭代的数字，有x个连在一起的c->xc, 直到无重复
        记录c, 当出现不同，则返回x（从0开始），c更新,res = res+x+c；相同则x+1，c不变；遍历完则return res = res+x+c;
        (x=1时忽略)
        ----
        为1就直接返回1
        '''
        if(n == 1):
            return str(1)
        while n != 1:
            res = ''
            n = n - 1
            pre = Solution().countAndSay(n)
            x = 0
            flag = pre[0]
            first = 0
            for c in pre:# 1/ 2 1 1
                if(first == 0):
                    first = 1
                if(c != flag):
                    res = res+Solution().ifZero(first, x)+flag # 11/ 12/
                    flag = c # 2/ 1
                    x = 1
                    continue
                x += 1
            res = res+Solution().ifZero(first, x)+c
            print(res)
            return res
        

