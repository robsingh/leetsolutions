'''
On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. 
Return the minimum time in seconds to visit all the points in the order given by points.

You can move according to these rules:

In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.
'''

'''
Approach: 
Distance between two points is maximum difference of one coordinate.

If the next node is +10x and -5y away, it is going to take exactly 10 steps, 
because you can move 1x at a time and the difference in 'y' is made up of diagonal moves during the process of
overcoming the difference in 'x'.

Time: O(N)
Space: O(1)
'''

class Solution:
    def minTimeToVisitAllPoints(self, points) -> int:
        result = 0
        x1, y1 = points.pop()
        while points:
            x2, y2 = points.pop()
            result += max(abs(y2-y1), abs(x2-x1))
            x1, y1 = x2, y2
        return result
    
sol = Solution()
print(sol.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))