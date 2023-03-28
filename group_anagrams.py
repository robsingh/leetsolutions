"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

from typing import List

class Solution:
    def groupAnagrams(self, strs:List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]

        return list(groups.values())





sol = Solution()
print(sol.groupAnagrams(strs=["eat","tea","tan","ate","nat","bat"]))