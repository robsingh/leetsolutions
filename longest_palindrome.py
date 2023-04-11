"""
Given a string s, return the longest palindromic substring in s.

A string is palindromic if it reads the same forward and backward.
"""

class Solution:
    def longestPalindrome(self,s:str) -> str:
        n = len(s)
        max_len = 1
        start = 0

        dp = [[False]*n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True

        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                max_len = 2
                start = i

        for k in range(3, n+1):
            for i in range(n-k+1):
                j = i + k - 1
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    if k > max_len:
                        max_len = k
                        start = i

        return s[start:start+max_len]



sol = Solution()
s = "cbbd"
print(sol.longestPalindrome(s))