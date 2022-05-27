# Source : https://leetcode.com/problems/longest-repeating-character-replacement/
# Author : Razhan Hameed
# Date   : 2022-05-27

##################################################################################################### 
#
# You are given a string s and an integer k. You can choose any character of the string and change it 
# to any other uppercase English character. You can perform this operation at most k times.
# 
# Return the length of the longest substring containing the same letter you can get after performing 
# the above operations.
# 
# Example 1:
# 
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# 
# Example 2:
# 
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# 
# Constraints:
# 
# 	1 <= s.length <= 10^5
# 	s consists of only uppercase English letters.
# 	0 <= k <= s.length
#####################################################################################################

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        windowStart = 0
        maxLen = 0
        maxRepeatChar = 0
        char = {}
        for windowEnd in range(len(s)):
            rightChar = s[windowEnd]
            char[rightChar] = char.get(rightChar, 0) + 1
            maxRepeatChar = max(maxRepeatChar, char[rightChar]) 
            
            if (windowEnd - windowStart + 1 - maxRepeatChar) > k :
                leftChar = s[windowStart]
                char[leftChar] -= 1
                windowStart += 1
               
            maxLen = max(maxLen, windowEnd - windowStart + 1)
        return maxLen
            
