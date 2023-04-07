"""
Given a binary tree, determine if it is height-balanced.
"""
from typing import Optional,List
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self,root:Optional[TreeNode]) -> bool:
        def height(node):
            if node is None:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)

            return 1 + max(left_height,right_height)
        
        def is_balanced_helper(node):
            if node is None:
                return True
            left_height = height(node.left)
            right_height = height(node.right)

            if abs(left_height - right_height) > 1:
                return False
            return is_balanced_helper(node.left) and is_balanced_helper(node.right)
        

        return is_balanced_helper(root)
    

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
print(sol.isBalanced(root))



