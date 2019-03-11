#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (34.61%)
# Total Accepted:    208.7K
# Total Submissions: 601.6K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n3'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
# 
# 
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
# 
# 
# Example 1:
# 
# 
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 3
# Output: true
# 
# 
# Example 2:
# 
# 
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 13
# Output: false
# 
#
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        从右上角开始，若target > a => col - 1
                     target < a => row + 1
        直到target = a ,return
        '''
        rows = len(matrix)
        if(rows == 0):
            return False
        cols = len(matrix[0])
        if(cols == 0):
            return False
        print(rows, cols)
        row = 0
        col = cols - 1
        a = matrix[row][col]
        print(a)
        while(row < rows and col >= 0):
            a = matrix[row][col]
            if(target == a):
                return True
            elif(target < a):
                col -= 1
            else:
                row += 1
        return False

