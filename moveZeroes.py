"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order
of the non-zero elements. 

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

class Solution:
    def moveZ(self, nums):
        # this approach returns a list 
        # count_zero = nums.count(0)
        # nums[:] = [num for num in nums if num != 0]
        # nums.extend([0] * count_zero)
        # return nums
    
        # in-place approach - using Two-pointer
        lastNonZeroFoundAt = 0
        for cur in range(len(nums)):
            if nums[cur] != 0:
                nums[lastNonZeroFoundAt], nums[cur] = nums[cur], nums[lastNonZeroFoundAt]
                lastNonZeroFoundAt += 1


sol = Solution()
nums = [0,1,0,3,12]
sol.moveZ(nums)
print(nums)