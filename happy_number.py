'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

class Solution:
    def isHappy(self, n):
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            number_split = list(map(int, str(n)))
            sum_squares = sum(x ** 2 for x in number_split)
            n = sum_squares

        return n == 1

sol = Solution()
print(sol.isHappy(n=10))