"""
Given the root of a binary tree, check whether it is a mirror of itself 
(i.e., symmetric around its center).
"""
from typing import Optional
class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
class Solution:
    def isSymmetric(self, root:Optional[TreeNode]) -> bool:
        def isMirror(node1,node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return (node1.val == node2.val and 
                    isMirror(node1.left, node2.right) and
                    isMirror(node1.right, node2.left))
        
        if not root:
            return True
        return isMirror(root.left,root.right)



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

sol = Solution()
print(sol.isSymmetric(root))