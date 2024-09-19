'''
Given two integers a and b, return the sum of the two integers without using the operators + and -.
'''

class Solution:
    def getSum(self, a:int, b:int) -> int:
        MAX = 0x7FFFFFFF
        MIN = 0x80000000
        MASK = 0xFFFFFFFF

        while b != 0:
            a,b = (a^b) & MASK, ((a&b) << 1) & MASK
        
        return a if a <= MAX else ~(a ^ MASK)

sol = Solution()
a, b = 2, 9
print(sol.getSum(a,b))