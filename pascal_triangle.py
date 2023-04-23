"""
Given an integer numRows, return the first numRows of Pascal's triangle.

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""
from typing import List
class Solution:
    def generate(self,numRows:int) -> List[List[int]]:
        """
        Generate the first numRows of Pascal Traingle.

        Args:
            numRows (int): number of rows to generate

        Return:
            List[int] : list of lists representing the generated pascal triangle.
        """
        triangle = []
        for i in range(numRows):
            # create a row of 1's wih length (i+1)
            row = [1] * (i+1)
            for j in range(1,i):
            # calculate each element in the current row by summing the two corresponding elements from the previous row
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
        return triangle
        

sol = Solution()
numRows = 5
print(sol.generate(numRows))
