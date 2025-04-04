"""
Given a string 's' containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Input: s = "()[]{}"
Output: true
"""
"""
Time Complexity : O(n)
Space Complexity: O(n)
"""
"""
1. Mapping of opening to closing brackets.
2. Process each char one by one.
3. For opening brackets, add them to stack.
4. For closing brackets, checks if it matches with most recent opening bracket.
5. Make sure all opening brackets were closed.
"""
class Solution:
    def isValid(self, s:str) -> bool:
        # dictionary to map opening bracket to their corresponding closing brackets
        brackets = {
            '[': ']',
            '{' : '}',
            '(': ')'
        }

        # Stack to keep track of opening brackets
        stack = []

        # process each character in the input string
        for char in s:
            # if it is a opening bracket
            if char in brackets: # this checks if char is a key in the dictionary
                stack.append(char)
            
            # If it's a closing bracket
            elif char in brackets.values():
                # What happens if we encounter a closing bracket when our stack is empty?
                if not stack:
                    return False
                
                # get most recent opening bracket
                last_opening = stack.pop()

                # Check if the current closing bracket matches the expected closing bracket
                if brackets[last_opening] != char:
                    return False
        
        # At the end, check if there are any unclosed opening brackets
        return len(stack) == 0


sol = Solution()
print(sol.isValid(s="(]"))
print(sol.isValid(s="[()]"))
print(sol.isValid(s="{(]}"))