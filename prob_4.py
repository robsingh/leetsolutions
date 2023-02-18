"""Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n))"""

"""
To find median,
1. we need to sort them.
2. If count of the array is odd -> median is the middle value.
3. If count of the array is even -> median is the average of two middle values.
"""

"""
Input: nums1 = [3,2], nums2 = [2]
Output: 2.0000
final array = [1,2,3] -> median is 2 (2 being the middle value and count is odd)

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Final array = [1,2,3,4] -> median = (2+3)//2 = 2.5 (2,3 being the middle values and count is even)
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        # make sure that nums1 is always the shorter array
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        # binary search
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            # i is too small, increase i
            if i < m and nums2[j-1] > nums1[i]:
                imin = i + 1
            # i is too big, decrease i
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            # i is perfect
            else:
                # calculate max_of_left
                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])
                # if the total length is odd, the median is the max_of_left
                if (m + n) % 2 == 1:
                    return max_of_left
                # calculate min_of_right
                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])
                # if the total length is even, the median is the average of max_of_left and min_of_right
                return (max_of_left + min_of_right) / 2     



sol = Solution()
print(sol.findMedianSortedArrays(nums1=[3,2], nums2=[2]))