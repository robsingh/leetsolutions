"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every 
node never differs by more than one.

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
"""
from typing import List,Optional

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

"""
1. if array is empty, then return Null
"""

class Solution:
    def arraytoBST(self,nums:List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        
        root.left = self.arraytoBST(nums[:mid])
        root.right = self.arraytoBST(nums[mid+1:])

        return root
