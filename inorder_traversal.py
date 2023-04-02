"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Input: root = [1,null,2,3]
Output: [1,3,2]
"""
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root:Optional[TreeNode]) -> List[int]:
        result = []
        def traverse(node,result):
            if node is not None:
                traverse(node.left,result)
                result.append(node.val)
                traverse(node.right,result)
        traverse(root,result)
        return result
    
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

sol = Solution()
print(sol.inorderTraversal(root))

