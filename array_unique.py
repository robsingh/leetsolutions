'''
You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

Return the minimum number of moves to make every value in nums unique.

Example 1:

Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].
Example 2:

Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
'''

class Solution:
    def minIncrementForUnique(self, nums):
        nums.sort()
        moves = 0

        for i in range(1, len(nums)):
            # if current element is not greater than previous element
            if nums[i] <= nums[i-1]:
                increment = nums[i-1] - nums[i] + 1
                nums[i] += increment
                moves += increment

        return moves


sol = Solution()
print(sol.minIncrementForUnique(nums = [1,2,2]))