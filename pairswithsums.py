'''
You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.
Define a pair (u, v) which consists of one element from the first array and one element from the second array.
Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Example:
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
'''
import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k:int):
        if not nums1 or not nums2 or k == 0:
            return []
        
        min_heap = []
        result = []
        
        #initialize the heap
        for i in range(min(k, len(nums1))):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
        
        while min_heap and len(result) < k:
            sum_val, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j+1], i, j+1))
        
        return result


sol = Solution()
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
print(sol.kSmallestPairs(nums1, nums2, k))