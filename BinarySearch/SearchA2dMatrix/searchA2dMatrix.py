# Source : https://leetcode.com/problems/search-a-2d-matrix/
# Author : Razhan Hameed
# Date   : 2022-04-20

##################################################################################################### 
#
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. 
# This matrix has the following properties:
# 
# 	Integers in each row are sorted from left to right.
# 	The first integer of each row is greater than the last integer of the previous row.
# 
# Example 1:
# 
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# 
# Example 2:
# 
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
# 
# Constraints:
# 
# 	m == matrix.length
# 	n == matrix[i].length
# 	1 <= m, n <= 100
# 	-10^4 <= matrix[i][j], target <= 10^4
#####################################################################################################


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        m = len(matrix)
        n = len(matrix[0])
        
        top, bottom = 0, m - 1
        while top <= bottom:
            row = (top + bottom) // 2
            
            # if target is larger than the last element of this row then it is in the rows below
            if target > matrix[row][-1]:
                top = row + 1
            # if target is small than the first element of this row then it is in the row above
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
       
        if not (top <= bottom):
            return False
        
        # row = (top + bottom // 2) # this means the target is in the current row
        row = top + ((bottom - top ) // 2) # this will solve the overflow problem
        l, r = 0, n - 1
            
        while l <= r:
            mid = l + ((r - l) // 2)
            print(row, mid)
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
              
        return False
            
        
        
        
