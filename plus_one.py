"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""
"""
Thought process:
We need to add 1 to the larger integer which is present at the least significant digit(rightmost digit)
If resulting digit is 10, we need to carry over the 1 to the next digit to the left, repeat it
until no carry is left. 

"""
from typing import List
class Solution:
    def plusOne(self, digits:List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
            if not carry:
                break
        if carry:
            digits.insert(0, carry)
        return digits
    

sol = Solution()
print(sol.plusOne(digits=[1,2,9]))