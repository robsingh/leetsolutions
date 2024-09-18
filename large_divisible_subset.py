'''
Given a set of distinct positive integers nums, return the largest subset answer such that 
every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.
'''

class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()
        n = len(nums)
        dp = [[] for _ in range(n)]
        for i in range(n):
            max_subset = []
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) > len(max_subset):
                    max_subset = dp[j]
            dp[i] = max_subset + [nums[i]]

        return max(dp, key=len)


sol = Solution()
nums = [1,2,4,8]
print(sol.largestDivisibleSubset(nums))