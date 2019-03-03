#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (40.35%)
# Total Accepted:    362.8K
# Total Submissions: 896.7K
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.
# 
# You may assume no duplicates in the array.
# 
# Example 1:
# 
# 
# Input: [1,3,5,6], 5
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [1,3,5,6], 2
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: [1,3,5,6], 7
# Output: 4
# 
# 
# Example 4:
# 
# 
# Input: [1,3,5,6], 0
# Output: 0
# 
# 
#
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        一个计数器，若nums[i]<target,nums[i+1]>target则返回i+1;
                    nums[i+1]<target, 进入下一轮循环; nums[i+1]==target,return i+1
        ----
        1. 数组全部小，循环外，返回i+1
        2. 数组全部大，首先和零比较
        3. 空数组
        '''
        if(len(nums) == 0):
            return 0
        i = 0
        val = 0
        if(nums[0] >= target):
            return 0
        while i < len(nums)-1:
            if(nums[i+1] >= target):
                return i+1
            else:
                i += 1
                continue
        return i+1 

