#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
#
# algorithms
# Easy (39.26%)
# Total Accepted:    527.1K
# Total Submissions: 1.3M
# Testcase Example:  '[1,1,2]'
#
# Given a sorted array nums, remove the duplicates in-place such that each
# element appear only once and return the new length.
# 
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
# 
# Example 1:
# 
# 
# Given nums = [1,1,2],
# 
# Your function should return length = 2, with the first two elements of nums
# being 1 and 2 respectively.
# 
# It doesn't matter what you leave beyond the returned length.
# 
# Example 2:
# 
# 
# Given nums = [0,0,1,1,1,2,2,3,3,4],
# 
# Your function should return length = 5, with the first five elements of nums
# being modified to 0, 1, 2, 3, and 4 respectively.
# 
# It doesn't matter what values are set beyond the returned length.
# 
# 
# Clarification:
# 
# Confused why the returned value is an integer but your answer is an array?
# 
# Note that the input array is passed in by reference, which means modification
# to the input array will be known to the caller as well.
# 
# Internally you can think of this:
# 
# 
# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeDuplicates(nums);
# 
# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len
# elements.
# for (int i = 0; i < len; i++) {
# print(nums[i]);
# }
# 
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        给一个tmp标记第一个数，for循环里对比：若和tmp相同则del这个数，tmp不变，进入下一轮；
            若和tmp不同，则tmp更新为这个数，进入下一轮
        ---
        len = 0或者1，直接返回
        '''
        if(len(nums) <= 1):
            return len(nums)
        tmp = nums[0]
        i = 1
        while i < len(nums): # 链表可以用是否存在判断，因为它的末尾连着None，但数组没了就是没了，用index获取会报错
            if(nums[i] == tmp):
                del nums[i]
                continue
            tmp = nums[i]
            i += 1
        return len(nums)   
        '''
        1. 链表可以用是否存在判断，因为它的末尾连着None，但数组没了就是没了，用index获取会报错
        2. 不能新建数组，对原数组进行操作的时候，记得数组长度是动态变化的！
        3. 该跳出循环的是时候看看自增的变量有没有停止自增
        4. in-place algorithm千万不能因为粗心漏掉了next元素的判断
        ''' 

