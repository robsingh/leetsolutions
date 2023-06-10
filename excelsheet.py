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
"""
Thought process:
1. Initialize an empty string to store the column title.
2. While the columnNumber is greater than 0:
    -> Subtract 1 from the columnNumber to adjust it to a zero-based index.
    -> calculate the remainder of the columnNumber divided by 26. This will give us the index of the corresponding letter in the alphabet.
    -> Convert the index to a letter by adding it to the ASCII value of 'A'. (use chr())
    -> add the letter to the beginning of the column string. 
    -> divide the columnNumber by 26, discarding any remainder, to move to the next digit. 
3. Return the column title string. 

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