"""
Given an integer array nums and an integer k, 
return the k most frequent elements. You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]
"""

from typing import List
from collections import Counter

class Solution:
    def topKfrequent(self, nums: List[int], k:int) -> List[int]:
        seen = Counter(nums)
        # result = [(key,value) for key,value in seen.items() if value == (k)]
        sorted_seen = sorted(seen.items(), key=lambda x:x[1], reverse=True)
        return [sorted_seen[i][0] for i in range(k)]


sol = Solution()
print(sol.topKfrequent(nums=[1,1,1,2,2,3], k=2))