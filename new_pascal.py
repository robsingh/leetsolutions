"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

Input: rowIndex = 3
Output: [1,3,3,1]
"""
from typing import List
class Solution:
    def getRow(self, rowIndex:int) -> List[int]:
        result = [1] * (rowIndex + 1)
        for i in range(1,rowIndex):
            result[i] = int(result[i-1] * (rowIndex-i+1) / i)
        
        return result

sol = Solution()
rowIndex = 4
print(sol.getRow(rowIndex))