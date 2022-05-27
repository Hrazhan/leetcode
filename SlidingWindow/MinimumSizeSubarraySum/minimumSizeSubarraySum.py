# Source : https://leetcode.com/problems/minimum-size-subarray-sum
# Author : Razhan Hameed
# Date   : 2022-05-27

##################################################################################################### 
#
# Given an array of positive integers nums and a positive integer target, return the minimal length 
# of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or 
# equal to target. If there is no such subarray, return 0 instead.
# 
# Example 1:
# 
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# 
# Example 2:
# 
# Input: target = 4, nums = [1,4,4]
# Output: 1
# 
# Example 3:
# 
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
# 
# Constraints:
# 
# 	1 <= target <= 10^9
# 	1 <= nums.length <= 10^5
# 	1 <= nums[i] <= 10^5
# 
# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time 
# complexity is O(n log(n)).
#####################################################################################################


import math

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        minLength = float('inf')
        windowSum = 0
        windowStart = 0
        for windowEnd in range(0, len(nums)):
            windowSum += nums[windowEnd]
            # shrink the window as small as possible until the sliding window is smaller than the target
            while windowSum >= target:
                minLength = min(minLength, windowEnd - windowStart + 1)
                windowSum -= nums[windowStart]
                windowStart += 1
        
        if minLength == float('inf'):
            return 0
        return minLength
       
            
