"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""
import re

class Solution:
    def isPalindrome(self, s:str) -> bool:
        """
        \W matches any non-alphanumeric character and
        underscores with an empty string.
        """
        conv_string = re.sub('[\W_]+', '', s).lower().strip()
        rev_conv = conv_string[::-1]

        if conv_string == rev_conv:
            return True
        else:
            return False

sol = Solution()
s = "A man, a plan, a canal: Panama"
print(sol.isPalindrome(s))