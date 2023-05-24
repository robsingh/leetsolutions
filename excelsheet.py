"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
Input: columnNumber = 1
Output: "A"

Input: columnNumber = 701
Output: "ZY"

Constraints:

1 <= columnNumber <= 231 - 1
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1
            letter_index = columnNumber % 26
            result = chr(ord('A') + letter_index) + result
            columnNumber //= 26
        return result



sol = Solution()
columnNumber = 701
print(sol.convertToTitle(columnNumber))