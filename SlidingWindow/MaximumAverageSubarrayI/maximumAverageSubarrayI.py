# Source : https://leetcode.com/problems/maximum-average-subarray-i/
# Author : Razhan Hameed
# Date   : 2022-05-26

##################################################################################################### 
#
# You are given an integer array nums consisting of n elements, and an integer k.
# 
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return 
# this value. Any answer with a calculation error less than 10^-5 will be accepted.
# 
# Example 1:
# 
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# 
# Example 2:
# 
# Input: nums = [5], k = 1
# Output: 5.00000
# 
# Constraints:
# 
# 	n == nums.length
# 	1 <= k <= n <= 10^5
# 	-10^4 <= nums[i] <= 10^4
#####################################################################################################

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        result = -1000
        _sum  = 0.0
        windowStart = 0
        for windowEnd in range(len(nums)):
            _sum += nums[windowEnd]
            
            if windowEnd >= k - 1:
                result = max(result, _sum/k)
                _sum -= nums[windowStart]
                windowStart += 1

        return result
