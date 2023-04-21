"""
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""
"""
Thinking:
1. Check if an integer is a 32-bit signed integer
 Do not consider trailing zeroes.

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
        def is_32_bit_signed(x):
            return isinstance(x,int) and -2 ** 31 <= x <= 2**31 - 1
        
        if is_32_bit_signed(x):
            reversed_str =  str(x)[::-1]
            # check if reversed string represents a 32-bit signed integer
            if is_32_bit_signed(int(reversed_str)):
                return int(reversed_str)
            
        # if input is not a 32-bit signed integer or reversed value goes  outside the 32-bit range - return 0

        return 0

sol = Solution()
x = 120
print(sol.reverse(x))