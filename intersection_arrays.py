"""
Given two integer arrays num1 and num2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may
return the result in any order. 

nums1 = [1,2,2,1], 
num2 = [2,2]

Output: [2,2]
"""
from typing import List

class Solution:
    def intersect(self, nums1:List[int], nums2:List[int]):
        freq_map = {}
        for num in nums1:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        intersection = []
        for num in nums2:
            if num in freq_map and freq_map[num] > 0:
                intersection.append(num)
                freq_map[num] -= 1
        return intersection
                    

sol = Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(sol.intersect(nums1, nums2))