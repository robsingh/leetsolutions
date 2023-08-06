"""
Given an unsorted array of integers nums, return the length of the 
longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109

"""


from typing import List

class Solution:
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
        
    #     num_set = set(nums)
    #     max_length = 1

    #     for num in num_set:
    #         # check if current number is start of the sequence
    #         if num - 1 not in num_set:
    #             current_num = num
    #             current_length = 1

    #             # find the length of consecutive sequence
    #             while current_num + 1 in num_set:
    #                 current_num += 1
    #                 current_length += 1

    #             max_length = max(max_length, current_length)
            
    #     return max_length
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)
        longest = 1
        
        for num in nums:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                longest = max(longest, length)
        return longest





sol = Solution()
nums = [0,3,7,2,5,8,4,6,0,1]
print(sol.longestConsecutive(nums))