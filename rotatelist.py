"""
Given an integer array nums, rotate the array to the right by 'k' steps, where k is non-negative.

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

nums: [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
"""
from typing import List
class Solution:
    def rotate(self, nums:List[int], k:int):
        # n = len(nums)
        # k %= n  # if k is greater than n, take the remainder
        # nums[:] = nums[-k:] + nums[:-k]
        # return nums

        #O(1)
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n-1) #reverse entire array
        self.reverse(nums, 0, k-1) #reverse first k elements
        self.reverse(nums, k, n-1) #reverse last n-k elements

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


nums = [-1,-100,3,99]
k = 2
sol = Solution()
sol.rotate(nums, k)
print(nums)