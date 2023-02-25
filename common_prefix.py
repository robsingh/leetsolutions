"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""   

"""
Approach: 
Compare the characters of the input one by one
Builds a common prefix string by appending characters that matches across all the strings.
When it encounters a non-matching character or end of the string, it returns the current prefix string.
If all characters matches across all the strings, it returns the entire first string as longest common prefix.


"""
from typing import List
class Solution:
    def longestCommonPrefix(self, strs:List[str]) -> str:
        prefix = ""
        if not strs:
            return prefix
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return prefix
            prefix += char
        return prefix



sol = Solution()
print(sol.longestCommonPrefix(strs=["flower","flow","flight"]))
