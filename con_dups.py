"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums:List[int]) -> bool:
        # dict = {}
        # for i in nums:
        #     if i in dict:
        #         dict[i] += 1
        #     else:
        #         dict[i] = 1
        
        # for key, value in dict.items():
        #     if value > 1:
        #         return True
        # return False
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    

sol = Solution()
print(sol.containsDuplicate(nums=[1,2,2,3,4,1]))