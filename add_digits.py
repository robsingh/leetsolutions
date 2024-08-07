'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:

Input: num = 38
Output: 2

Explanation:
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
'''

class Solution:
    def addDigits(self, num):
        while num >= 10:
            num = sum(int(digit) for digit in str(num))
        return num

sol = Solution()
num = 38
print(sol.addDigits(num))

