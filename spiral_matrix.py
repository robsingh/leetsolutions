'''
Given an m*n matrix, return all the elements of the matrix in spiral order.
example:
matrix = [[1,2,3], [4,5,6], [7,8,9]]
o/p = [1,2,3,6,9,8,7,4,5]
'''

'''
Simulate the movement in 4 directions:
left -> right
top -> bottom
right -> left
bottom -> top

O(N)
'''

class Solution:
    def spiralMatrix(self, matrix):
        result = []
        while matrix:
            #add first row of the matrix
            result += (matrix.pop(0))

            #append last element of all lists in order
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())

            #add reverse of last row
            if matrix:
                result += (matrix.pop()[::-1])

            #append first element of all rows in reverse
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))

        return result
    

sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(sol.spiralMatrix(matrix))