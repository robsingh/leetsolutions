"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.

Input: p = [1,2,3], q = [1,2,3]
Output: true
"""
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self,p:Optional[List],q:Optional[List]) -> bool:
       # if both trees are none, they're identical
       if not p and not q:
           return True
       # if one of the Trees is none, they're not identical
       if not p or not q:
           return False
       # if roots have different values, they're not identical
       if p.val != q.val:
           return False
       # recursively check if left and right subtrees are identical
       return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)


sol = Solution()
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))

print(sol.isSameTree(p,q))