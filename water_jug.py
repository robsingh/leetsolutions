'''
You are given two jugs with capacities x liters and y liters. You have an infinite water supply. 
Return whether the total amount of water in both jugs may reach target using the following operations:

Fill either jug completely with water.
Completely empty either jug.
Pour water from one jug into another until the receiving jug is full, or the transferring jug is empty.
'''
import math

class Solution:
    def canMeasureWater(self, x:int, y:int, target:int) -> bool:
        # if target is greater than sum of x and y, it is impossible
        if target > x + y:
            return False
        # if target is 0, it is possible
        if target == 0:
            return True
        
        return target % math.gcd(x,y) == 0


sol = Solution()
print(sol.canMeasureWater(x=3, y=5, target=4))