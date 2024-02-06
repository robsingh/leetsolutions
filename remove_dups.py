"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. (tuple, set, dictionary)
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the 
array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""
from typing import List
class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
        # # initialize two pointers, one for the current position and one for the last non-duplicate position
        # i = 0
        # j = 0
        # while i < len(nums):
        #     # if current element is not a duplicate, move it to the last non-duplicate position
        #     if nums[i] != nums[j]:
        #         j += 1
        #         nums[j] = nums[i]
        #     i += 1
        # # length of the array is the index of the last non-duplicate element plus one
        # return j + 1

    def removeDuplicates(self, nums:List[int]) -> int:
        if not nums:
            return 0
        pointer = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[pointer] = nums[i]
                pointer += 1

        return pointer
    
    # time complexity - O(n) - since we iterate through the array once, the time complexity is linear. 

sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
