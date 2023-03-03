"""
Given a string 's' containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

"""

class Solution:
    def isValid(self,s:str) -> bool:
        diction = {'(':')','{':'}','[':']'}
        stack = []
        for char in s:
            if char in diction:
                stack.append(char)
            elif not stack or diction[stack.pop()] != char:
                return False
        return not stack


sol = Solution()
print(sol.isValid(s="(]"))
print(sol.isValid(s="(]"))
print(sol.isValid(s="(]"))