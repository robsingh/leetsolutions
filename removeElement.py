"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the
result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates, then the first k elements of nums 
should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array
in-place with O(1) extra memory.
"""
from typing import List

class Solution:
    def removeElement(self, nums:List[int], val:int) -> int:
        k = 0  # to keep track of the last index of the array
        for i in range(len(nums)):
            # if current element is not equal to val, then it should be included in modified array
            if nums[i] != val:
                nums[k] = nums[i] #add the current element to the modified array at index k
                k += 1
        return k
    
    # def removeElement(self, nums:List[int], val:int) -> int:
    #     # iterating through the array from both ends
    #     left, right = 0, len(nums) - 1
    #     while left <= right:
    #         if nums[left] == val:
    #             nums[left], nums[right] = nums[right], nums[left]
    #             right -= 1
    #         else:
    #             left += 1
    #     return left
    
    
sol = Solution()
print(sol.removeElement(nums=[3,2,2,3], val=3))