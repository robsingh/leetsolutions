"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]...nums[i])
Return the running sum of nums. 

Example:
nums = [1,2,3,4]
Output = [1,3,6,10]

nums = [1,1,1,1,1]
Output = [1,2,3,4,5]

nums = [3,1,2,10,1]
Output = [3,4,6,16,17]
"""

from typing import List
class Solution:
    def runningSum(self, nums:List[int]) -> List[int]:
        running_sum = []
        total = 0
        for num in nums:
            total += num
            running_sum.append(total)
        return running_sum



sol = Solution()
nums = [3,1,2,10,1]
print(sol.runningSum(nums))
