"""
Given two binary strings a and b, return their sum as a binary string.
A binary string is a sequence of bytes.

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

Convert to decimal and binary first?

Input: a = "11", b = "1"
Output: "100"

Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution:
    def addBinary(self, a:str, b:str) -> str:
        result = ""
        # converting to int
        a_list = [int(c) for c in a]
        b_list = [int(c) for c in b]

        while len(a_list) < len(b_list):
            a_list.insert(0,0)
        while len(b_list) < len(a_list):
            b_list.insert(0,0)

        carry = 0

        for i in range(len(a_list)-1, -1,-1):
            digit_sum = a_list[i] + b_list[i] + carry
            if digit_sum == 2 or digit_sum == 3:
                digit_sum -= 2
                carry = 1
            else:
                carry = 0
            result += str(digit_sum)

        if carry == 1:
            result += '1'
        
        result = result[::-1]
        return result
    

sol = Solution()
print(sol.addBinary(a='1010',b='1011'))