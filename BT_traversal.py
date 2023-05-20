"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.


Input: root = [1,null,2,3]
Output: [1,2,3]

Input: root = []
Output: []
"""
from typing import Optional, List
class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preOrderTraversal(self, root:Optional[TreeNode]) -> List[int]:
        result = []
        self.preOrderTraversalRecursive(root,result)
        return result
    
    def preOrderTraversalRecursive(self, node: Optional[TreeNode], result: List[int]):
        if node is None:
            return
        
        result.append(node.val) #visit the current node
        self.preOrderTraversalRecursive(node.left, result)
        self.preOrderTraversalRecursive(node.right, result)


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

sol = Solution()
preorder = sol.preOrderTraversal(root)
print(preorder)

