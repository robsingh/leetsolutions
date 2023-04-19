"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a 
root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Determine if there is a root to leaf path in the binary tree that sums up to targetSum.

        Args:
        - root : root node of binary tree
        - targetSum : an int representing targetSum

        Returns:
        - a boolean value
        """
        # if root node is None, there is no path that sums up to targetSum
        if not root:
            return False
        
        # if root node is a leaf node and its value equals targetSum return True
        if not root.left and not root.right and targetSum == root.val:
            return True
        
        # recursively check the left and right subtrees for paths that sum up to targetSum
        left = self.hasPathSum(root.left, targetSum - root.val)
        right = self.hasPathSum(root.right, targetSum - root.val)

        return left or right
  


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

sol = Solution()
targetSum = 22
print(sol.hasPathSum(root,targetSum))