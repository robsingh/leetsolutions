"""
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

class Solution:
    def reverse(self, x:int) -> int:
        """
        Reverses the digits of a signed 32-bit integer.

        Args:
            x(int): signed 32-bit integer to reverse

        Returns:
            int: reversed signed 32-bit integer, or 0 if the reversed value goes outside the 32-bit range.
        """
        # check if x is a 32-bit signed integer
        if x < -2 ** 31 or x > 2 ** 31 - 1:
            return 0
        
        #convert the integer to a string and reverse it
        str_x = str(x)
        if x < 0:
            reversed_x = int('-' + str_x[:0:-1])
        else:
            reversed_x = int(str_x[::-1])

        # check if reversed integer is a 32-bit signed integer
        if reversed_x < -2 ** 31 or reversed_x > 2 ** 31 - 1:
            return 0
        
        return reversed_x

sol = Solution()
x = 120
print(sol.reverse(x))