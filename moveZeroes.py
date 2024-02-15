"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order
of the non-zero elements. 

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

class Solution:
    def moveZ(self, nums):
        count_zero = nums.count(0)
        nums[:] = [num for num in nums if num != 0]
        nums.extend([0] * count_zero)
        return nums

sol = Solution()
nums = [0,1,0,3,12]
print(sol.moveZ(nums))