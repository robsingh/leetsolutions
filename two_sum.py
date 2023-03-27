"""
Given an array of integers nums and an integer target, return indices of the two numbers such that 
they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element
twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]
"""

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return nums[i], nums[j]
                else:
                    return "No pairs"





sol = Solution()
print(sol.twoSum(nums=[2,7,11,15], target=9))