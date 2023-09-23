"""
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
Input: columnTitle = "AB"
Output: 28

Input: columnTitle = "ZY"
Output: 701
 
Constraints:
1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
"""
class Solution:
    def titleToNumber(self, excelsheet):
        col_number = 0
        for char in excelsheet:
        # convert the character to its corresponding number
            char_value = ord(char) - ord('A') + 1
        # multiply the current column number by 26 and add the character value
            col_number = col_number * 26 + char_value
        return col_number

sol = Solution()
print(sol.titleToNumber(excelsheet='ZY'))