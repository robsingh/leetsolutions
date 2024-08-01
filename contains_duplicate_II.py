'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that
nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

class Solution:
    def containsDuplicate(self, nums, k):
        #dictionary to store the last index of each number
        num_dict = {}

        for index, num in enumerate(nums):
            if num in num_dict and index - num_dict[num] <= k:
                return True
            num_dict[num] = index

        return False
        

sol = Solution()
nums = [1,2,3,1]
k = 3

print(sol.containsDuplicate(nums, k))