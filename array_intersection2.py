'''
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
'''
from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        counts1 = Counter(nums1)
        counts2 = Counter(nums2)
        result = []

        #find the intersection by looking at the minimum frequency of each element
        for num in counts1:
            if num in counts2:
                result.extend([num] * min(counts1[num], counts2[num]))
        
        return result


sol = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(sol.intersect(nums1, nums2))