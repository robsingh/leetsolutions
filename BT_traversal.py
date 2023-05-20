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
    # recursive approach
    # def preOrderTraversal(self, root:Optional[TreeNode]) -> List[int]:
    #     result = []
    #     self.preOrderTraversalRecursive(root,result)
    #     return result
    
    # def preOrderTraversalRecursive(self, node: Optional[TreeNode], result: List[int]):
    #     if node is None:
    #         return
        
    #     result.append(node.val) #visit the current node
    #     self.preOrderTraversalRecursive(node.left, result)
    #     self.preOrderTraversalRecursive(node.right, result)
    # non-recursive approach (using stack)
    def preOrderTraversal(self, root:Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)

            # we push the right child first because in pre-order traversal the left subtree is processed
            # before the right subtree (this can be bypassed while using recursive approach)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(5)

sol = Solution()
preorder = sol.preOrderTraversal(root)
print(preorder)

