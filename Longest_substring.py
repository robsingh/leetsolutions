"""
Given a string s, find the length of the longest substring without repeating characters.
Input: s = 'abcabcbb'
Output: 3

s consists of English letters, digits, symbols and spaces.

sliding window technique is used below.
"""

class Solution:
    def lengthOfLongestSubstring(self,s:str) -> int:
        n = len(s)
        if n <= 1:
            return n
        
        # initializing the length of longest substring
        max_len = 0 
        # create a dictionary to keep track of the last index of each character       
        char_map = {}       
        left = 0           
        for right in range(n):    
            # if current character is already in char_map and its last index is within the current window
            if s[right] in char_map and char_map[s[right]] >= left:
                # move the left pointer to the next character after first occurence
                left = char_map[s[right]] + 1   

            char_map[s[right]] = right 

            # update the max_len variable with the length of the current window
            max_len = max(max_len, right-left+1)
        
        return max_len





sol = Solution()
print(sol.lengthOfLongestSubstring(s='bb'))