"""
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Constraints:
1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""

class Solution:
    def lengthOfLastWord(self, s:str) -> int:
        words = s.split()
        if not words:
            return 0
        return len(words[-1])

sol = Solution()
print(sol.lengthOfLastWord(s='   fly me   to   the moon  '))
