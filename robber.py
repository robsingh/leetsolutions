"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and 
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""
"""

"""
from typing import List

class Solution:
    def rob(self, nums:List[int]) -> int:
        # even_elements = sum(nums[::2])
        # odd_elements = sum(nums[1::2])

        # if even_elements > odd_elements:
        #     return even_elements
        # else:
        #     return odd_elements
        if not nums:
            return 0
        prev_max = 0
        curr_max = 0

        for money in nums:
            temp = curr_max
            curr_max = max(prev_max + money, curr_max)
            prev_max = temp

        return curr_max



nums = [1,2,1,1]
sol = Solution()
print(sol.rob(nums))