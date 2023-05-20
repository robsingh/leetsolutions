"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Input: root = [1,null,2,3]
Output: [3,2,1]
"""
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> List[int]:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if not root:
        #     return []
        
        # stack = []
        # result = []
        # curr = root

        # while stack or curr:
        #     if curr:
        #         stack.append(curr)
        #         curr = curr.left or curr.right
        #     else:
        #         node = stack.pop()
        #         result.append(node.val)
        #         if stack and stack[-1].left == node:
        #             curr = stack[-1].right
        
        # return result

        # recursive approach

        result = []
        self.postOrderRecursive(root,result)
        return result
    
    def postOrderRecursive(self, node:Optional[TreeNode], result:List[int]):
        if node:
            self.postOrderRecursive(node.left, result)
            self.postOrderRecursive(node.right, result)
            result.append(node.val)
    





root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

sol = Solution()
print(sol.postOrderTraversal(root))
