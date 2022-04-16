# Source : https://leetcode.com/problems/top-k-frequent-elements/
# Author : Razhan Hameed
# Date   : 2022-04-16

##################################################################################################### 
#
# Given an integer array nums and an integer k, return the k most frequent elements. You may return 
# the answer in any order.
# 
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
# 
# Constraints:
# 
# 	1 <= nums.length <= 10^5
# 	k is in the range [1, the number of unique elements in the array].
# 	It is guaranteed that the answer is unique.
# 
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's 
# size.
#####################################################################################################


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            freq[c].append(n) # n occurs c number of times
        
        output = []
        # loop through freq in descending order from the last index to zero
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                output.append(n)
                if len(output) == k:
                    return output
