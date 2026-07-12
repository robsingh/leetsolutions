"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

from typing import List
from collections import defaultdict

# O(n.k log k) - sorting method
# class Solution:
#     def groupAnagrams(self, strs:List[str]) -> List[List[str]]:
#         groups = {}
#         for s in strs:
#             key = ''.join(sorted(s))
#             if key in groups:
#                 groups[key].append(s)
#             else:
#                 groups[key] = [s]

#         return list(groups.values())

# sol = Solution()
# print(sol.groupAnagrams(strs=["eat","tea","tan","ate","nat","bat"]))

#linear scan - O(n.k)
def groupAnagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for character in s:
            count[ord(character) - ord('a')] += 1
        key = tuple(count)
        groups[key].append(s)
    return list(groups.values())

print(groupAnagrams(strs=["eat","tea","tan","ate","nat","bat"]))    