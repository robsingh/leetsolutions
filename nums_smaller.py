'''
Given the array nums, for each nums[i],find out how many numbers in the array are smaller than it. 
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array.
'''
from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums:List[int]) -> List[int]:
        temp = sorted(nums)
        result = []
        di = {}

        for i,num in enumerate(temp):
            if num not in di:
                di[num] = i
            
        for num in nums:
            result.append(di[num])
        
        return result


sol = Solution()
nums = [8,1,2,2,3]
print(sol.smallerNumbersThanCurrent(nums))