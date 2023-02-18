# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.
from typing import Counter, List

"""
use a counter to count the occurrences of each DISTINCT element
count distinct integers in arr (count of keys and values)
"""

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        ckeys = Counter(arr).keys()
        cvalues = Counter(arr).values()
        cset = set(cvalues)
        return len(ckeys) == len(cset)

sol = Solution()
print(sol.uniqueOccurrences([1,2,2,1,1,3]))

# one liner (short of above)
# return len(Counter(arr).keys()) == len(Counter(arr).values())