""" Given an array of integers nums and an integer target, return indices (index) of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order. """

"""
    Input: nums = [2,7,11,15], target: 9
    Output: [0,1]
    because nums[0] + nums[1] == 9 
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for idx, value in enumerate(nums):
            if target - value in values:
                return [values[target-value], idx]
            else:
                values[value] = idx


sol = Solution()
print(sol.twoSum(nums=[2,7,11,15], target = 9))
print(sol.twoSum(nums=[3,2,4], target = 6))