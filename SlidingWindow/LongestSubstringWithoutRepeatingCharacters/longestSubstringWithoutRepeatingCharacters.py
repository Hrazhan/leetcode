# Source : https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
# Author : Razhan Hameed
# Date   : 2022-04-19

##################################################################################################### 
#
# Given a string s, find the length of the longest substring without repeating characters.
# 
# Example 1:
# 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# 
# Example 2:
# 
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# Example 3:
# 
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# 
# Constraints:
# 
# 	0 <= s.length <= 5 * 10^4
# 	s consists of English letters, digits, symbols and spaces.
#####################################################################################################


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet = set()
        l, r = 0, 0
        result = 0
        
        while r < len(s):
            print(charSet)
            while s[r] in charSet:
                charSet.remove(s[l])
                l +=1
            charSet.add(s[r])
            result = max(result, r - l + 1)
            r += 1
        return result
    
