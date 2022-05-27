# Source : https://leetcode.com/problems/permutation-in-string/
# Author : Razhan Hameed
# Date   : 2022-05-27

##################################################################################################### 
#
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# 
# In other words, return true if one of s1's permutations is the substring of s2.
# 
# Example 1:
# 
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# 
# Example 2:
# 
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
# 
# Constraints:
# 
# 	1 <= s1.length, s2.length <= 10^4
# 	s1 and s2 consist of lowercase English letters.
#####################################################################################################

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        char = {}
        windowStart = 0
        matched = 0 
        
        for i in s1:
            if i not in char:
                char[i] = 0
            char[i] += 1
        
        for windowEnd in range(len(s2)):
            rightChar = s2[windowEnd]
            
            if rightChar in char:
                char[rightChar] -= 1
                if char[rightChar] == 0:
                    matched += 1
                
            if len(char) == matched:
                return True
            #If the window size is greater than the length of the pattern, shrink the window to make it equal to the size of the pattern. 
            # At the same time, if the character going out was part of the pattern, put it back in the frequency HashMap
            if windowEnd >= len(s1) - 1:
                leftChar = s2[windowStart]
                windowStart += 1
                if leftChar in char:
                    if char[leftChar] == 0:
                        matched -= 1
                    # char[leftChar] = char.get(leftChar, 0) + 1
                    char[leftChar] += 1
                
        return False
