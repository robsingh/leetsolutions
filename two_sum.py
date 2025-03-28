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

''''
* We use an empty dictionary to store value as keys and their indices as values.
* For each number in the array, we calculate the complement (target - num).
* If the ccomplement exist in the dictionary, we return its index along with the current index.
* Otherwise, we store the current number and its index in the dictionary.
'''

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        values = {}
        for key,value in enumerate(nums):
            if target - value in values:
                return [values[target-value], key]
            else:
                values[value] = key


sol = Solution()
print(sol.twoSum(nums=[2,7,11,15], target=9))