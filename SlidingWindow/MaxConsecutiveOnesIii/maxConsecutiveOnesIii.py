# Source : https://leetcode.com/problems/max-consecutive-ones-iii/
# Author : Razhan Hameed
# Date   : 2022-05-27

##################################################################################################### 
#
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the 
# array if you can flip at most k 0's.
# 
# Example 1:
# 
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# 
# Example 2:
# 
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# 
# Constraints:
# 
# 	1 <= nums.length <= 10^5
# 	nums[i] is either 0 or 1.
# 	0 <= k <= nums.length
#####################################################################################################

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        windowStart = 0
        maxLen = 0
        maxOneCount = 0
        
        for windowEnd in range(len(nums)):
            if nums[windowEnd] == 1:
                maxOneCount += 1  
                
            if (windowEnd - windowStart + 1 - maxOneCount) > k:
                if nums[windowStart] == 1:
                    maxOneCount -= 1
                windowStart += 1
            
            maxLen = max(maxLen, windowEnd - windowStart + 1)
        
        return maxLen
