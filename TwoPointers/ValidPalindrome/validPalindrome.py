# Source : https://leetcode.com/problems/valid-palindrome/
# Author : Razhan Hameed
# Date   : 2022-04-17

##################################################################################################### 
#
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
# removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric 
# characters include letters and numbers.
# 
# Given a string s, return true if it is a palindrome, or false otherwise.
# 
# Example 1:
# 
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# 
# Example 2:
# 
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# 
# Example 3:
# 
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
# 
# Constraints:
# 
# 	1 <= s.length <= 2 * 10^5
# 	s consists only of printable ASCII characters.
#####################################################################################################



# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         newStr = ""
#         for c in s:
#             if c.isalnum():
#                 newStr += c.lower()
#         return newStr == newStr[::-1]
    
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and not self.isAlphanum(s[left]):
                left +=1
            while right > left and not self.isAlphanum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            
            left = left + 1
            right =  right - 1
            
        return True
    
    def isAlphanum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
               ord('a') <= ord(c) <= ord('z') or
               ord('0') <= ord(c) <= ord('9'))
