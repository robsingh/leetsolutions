"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 steps
"""
"""
Base Case - if n == 1 or n == 2 -> return n
"""

class Solution:
    def climbStairs(self,n:int) -> int:
        if n == 1 or n == 2: 
            return n
        else:
            prev_prev = 1
            prev = 2
            for _ in range(3, n+1):
                curr = prev_prev + prev
                prev_prev = prev
                prev = curr
            return curr


sol = Solution()
print(sol.climbStairs(n=4))