"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according 
to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
from typing import List
class Solution:
    def isValid(self,board:List[List[str]]) -> bool:
        #check each row
        for row in board:
            digits = set()
            for digit in row:
                if digit != "." and digit in digits:
                    return False
                digits.add(digit)
        
        #check each column
        for col in range(9):
            digits = set()
            for row in range(9):
                digit = board[row][col]
                if digit != "." and digit in digits:
                    return False
                digits.add(digit)
        
        #check each sub-box
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                digits = set()
                for row in range(box_row,box_row+3):
                    for col in range(box_col, box_col+3):
                        digit = board[row][col]
                        if digit != "." and digit in digits:
                            return False
                        digits.add(digit)

        
        return True

sol = Solution()
board = [
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(sol.isValid(board))