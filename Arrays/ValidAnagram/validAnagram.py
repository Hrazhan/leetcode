# Source : https://leetcode.com/problems/valid-anagram/
# Author : Razhan Hameed
# Date   : 2022-04-16

##################################################################################################### 
#
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.
# 
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
# 
# Constraints:
# 
# 	1 <= s.length, t.length <= 5 * 10^4
# 	s and t consist of lowercase English letters.
# 
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such 
# a case?
#####################################################################################################


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True
