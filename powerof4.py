'''
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4^x.

'''

class Solution:
    def powerOfFour(self, n) -> bool:
        if n <= 0:
            return False
        while n % 4 == 0:
            n //= 4
        return n == 1


sol = Solution()
n = 16
print(sol.powerOfFour(n))