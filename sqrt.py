"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""

class Solution:
    def mysqrt(self, x:int) -> int:
        if (x == 0 or x == 1):
            return x
        i = 1
        res = 1
        while res <= x:
            i += 1
            res = i * i
        return i - 1


sol = Solution()
print(sol.mysqrt(x=627))