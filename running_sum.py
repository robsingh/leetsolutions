"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]

"""

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        current_sum = 0

        for num in nums:
            current_sum += num
            running_sum.append(current_sum)
        
        return running_sum
        



nums = [1,2,3,4]
sol = Solution()
print(sol.runningSum(nums))