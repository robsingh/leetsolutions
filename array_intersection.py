'''
Given two integer arrays nums1 and nums2, return an array of their intersection. 
The intersection of two arrays is defined as the set of elements that are present in both arrays.
Each element in the result must be unique and you may return the result in any order.

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
'''

class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))



sol = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(sol.intersection(nums1, nums2))