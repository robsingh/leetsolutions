"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""

class Solution:
    # def mysqrt(self, x:int) -> int:  #not so efficient - brute force
    #     if (x == 0 or x == 1):
    #         return x
    #     i = 1
    #     res = 1
    #     while res <= x:
    #         i += 1
    #         res = i * i
    #     return i-1

    #using binary search
    def mysqrt(self,x:int) -> int:
        if (x == 0 or x == 1):
            return x
        left = 1
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1
    


sol = Solution()
print(sol.mysqrt(x=8))