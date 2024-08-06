'''
Given an integer n, return true if it is a power of two. Otherwise, return false.
'''

class Solution:
    def isPowerOfTwo(self, n:int) -> bool:
       if n <= 0:
           return False
       return (n & (n-1)) == 0


sol = Solution()
n = 16
print(sol.isPowerOfTwo(n))