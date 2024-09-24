'''
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.
'''
# I have changed it little bit to incorporate everything in my solution i.e. defining the guess API too!

class Solution:
    def __init__(self, pick):
        self.pick = pick
        
    def guess(self, num:int) -> int:
        if num > self.pick:
            return -1
        elif num < self.pick:
            return 1
        else:
            return 0
        
    def guessNumber(self, n:int) -> int:
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            result = self.guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                high = mid - 1
            else:
                low = mid + 1
                

pick = 6
n = 10
sol = Solution(pick)
print(sol.guessNumber(n))