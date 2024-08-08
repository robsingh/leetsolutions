'''

Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 
2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 
8 is the missing number in the range since it does not appear in nums.

Constraints:
All the numbers of nums are unique.
n == nums.length
'''

class Solution:
    def missingNumber(self, nums) -> int:
        # O(n logn) approach
        # nums.sort()

        # for i in range(len(nums)):
        #     # if the current number does not match the index, return the index as missing number
        #     if nums[i] != i:
        #         return i
            
        # # if all numbers match their index, the missing number is n
        # return len(nums)

        # O(n)
        n = len(nums)
        total_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return total_sum - actual_sum



sol = Solution()
nums = [3,0,1]
print(sol.missingNumber(nums))