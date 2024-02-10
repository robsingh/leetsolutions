"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Input: nums = [2,2,1]
Output: 1

Input: nums = [4,1,2,1,2]
Output: 4

Input: nums = [1]
Output: 1
"""
from typing import List
from collections import Counter
class Solution:
    def singleNumber(self, nums:List[int]) -> int:
        # count_each = Counter(nums)
        # for key,value in count_each.items():
        #     if value == 1:
        #         return key
        
        #another method - more memory efficient since it is not iterating through a dict
        result = 0
        for num in nums:
            result ^= num
        return result

nums = [2,2,1]
sol = Solution()
print(sol.singleNumber(nums))