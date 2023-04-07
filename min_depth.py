"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the
nearest leaf node.

Note: A leaf is a node with no children.
"""
from typing import Optional
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def min_depth(self,root:Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self.min_depth(root.left)
        right_depth = self.min_depth(root.right)


        if not left_depth or not right_depth:
            return max(left_depth, right_depth) + 1
        
        return min(left_depth,right_depth) + 1


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
print(sol.min_depth(root))