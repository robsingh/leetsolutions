"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
from typing import List
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length_array = len(nums)
        element_counter = Counter(nums)
        for key, value in element_counter.items():
            if value > length_array/2:
                return key




# nums = [3,2,3]
nums = [2,2,1,1,1,2,2]
sol = Solution()
print(sol.majorityElement(nums))