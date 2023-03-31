"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.

Input: head = [1,1,2]
Output: [1,2]

Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return head
        
        unique = last = ListNode(head.val)
        current = head.next

        while current:
            if current.val != last.val:
                last.next = ListNode(current.val)
                last = last.next
            current = current.next
        
        return unique
    
head = ListNode(1, ListNode(2, ListNode(3, ListNode(3))))

sol = Solution()

unique_head = sol.deleteDuplicates(head)
while unique_head:
    print(unique_head.val)
    unique_head = unique_head.next