"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""
from typing import List
import unittest
class Solution:
    def containsDuplicate(self, nums:List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

sol = Solution()
# print(sol.containsDuplicate(nums=[1,2,2,3,4,1]))

class TestcontainsDuplicate(unittest.TestCase):
    def test_all_unique(self):
        self.assertFalse(sol.containsDuplicate([1,2,3,4]))
    
    def test_one_duplicate(self):
        self.assertTrue(sol.containsDuplicate([1,2,3,1]))
    
    def test_multiple_duplicates(self):
        self.assertTrue(sol.containsDuplicate([1,2,2,2,3,3]))

    def test_all_same(self):
        self.assertTrue(sol.containsDuplicate([4,4,4,4]))

    def test_empty_list(self):
        self.assertFalse(sol.containsDuplicate([]))
    
    def test_single_element(self):
        self.assertFalse(sol.containsDuplicate([5]))


if __name__ == '__main__':
    unittest.main()