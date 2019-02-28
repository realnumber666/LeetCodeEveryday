#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (25.24%)
# Total Accepted:    384.1K
# Total Submissions: 1.5M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
# 
# You may assume nums1 and nums2 cannot be both empty.
# 
# Example 1:
# 
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# 
# 
# Example 2:
# 
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5
# 
# 
#
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums_all = []
        i = 0
        j = 0
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        total_len = nums1_len + nums2_len
        while i <= (nums1_len - 1) or j <= (nums2_len - 1):
            if(j > (nums2_len - 1)):
                nums_all.append(nums1[i])
                i += 1
            elif(i > (nums1_len - 1)):
                nums_all.append(nums2[j])
                j += 1
            elif(nums1[i] >= nums2[j]):
                nums_all.append(nums2[j])
                j += 1
            else:
                nums_all.append(nums1[i])
                i += 1
        index = int(total_len/2)
        if(total_len % 2 == 1):
            return nums_all[int(index)]
        else:
            return (nums_all[index] + nums_all[index - 1])/2
        