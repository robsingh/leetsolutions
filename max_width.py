"""
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes),
where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that
level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.
"""
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthofBinaryTree(self,root:Optional[TreeNode]) -> int:
        """
        Calculates max width of a binary tree.

        Args: 
            root: root of the binary tree

        Returns:
            int: max width of a binary tree 
        """
        
        if not root:
            return 0
        max_width = 0
        # initialize the queue with root node and its index.
        queue = deque([(root,0)])

        while queue:
            level_size = len(queue)
            left_index = queue[0][1] # get index of leftmost node in current level.
            for i in range(level_size):
                node,index = queue.popleft() # get the next node and its index from the queue.
                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))
            # index of the last processed node is the index of rightmost node.
            right_index = index
            width = right_index - left_index + 1
            max_width = max(max_width, width)
        
        return max_width


root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)

sol = Solution()
print(sol.widthofBinaryTree(root))