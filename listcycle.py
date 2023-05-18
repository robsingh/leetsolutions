"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again 
by continuously following the next pointer. Internally, pos is used to denote the index of the node 
that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""
from typing import Optional
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head:Optional[ListNode]) -> bool:
        """
        slow pointer moves one nodes at a time.
        fast pointer moves two nodes at a time.

        If there is a cycle, these two pointers will eventually meet at the same node.
        If there is no cycle, 'fast' pointer will reach the end of the list, indicating there is no cycle.
        """
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True
    
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next     #creates a cycle

sol = Solution()
has_cycle = sol.hasCycle(head)

print(has_cycle)




