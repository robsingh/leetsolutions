"""

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.


The test cases are generated such that there are no cycles anywhere in the entire linked structure.
Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.


The judge will then create the linked structure based on these inputs and pass the two heads, 
headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. 
There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
- Note that the intersected node's value is not 1 because the nodes with value 1 in A and B 
(2nd node in A and 3rd node in B) are different node references. 
In other words, they point to two different locations in memory, 
while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory. d
"""
from typing import Optional
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        Find the intersection node of two linked lists.
        Args:
            headA: head node of first linked list
            headB: head node of second linked list
        Returns:
            Intersection node if found, None otherwise.
        """

        # calculate the length of both linked lists
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)

        # calculate the difference in lengths
        diff = abs(lenA - lenB)

        # move the pointer of the longer linked list ahead by the difference in lengths
        if lenA > lenB:
            while diff > 0:
                headA = headA.next
                diff -= 1
        else:
            while diff > 0:
                headB = headB.next
                diff -= 1

        # traverse both linked lists simultaneously until a common node is found or end is reached
        while headA is not None and headB is not None:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        # no intersection found
        return None

    
    def getLength(self, head: ListNode) -> int:
        """
        Calculate the length of linked list.
        Args:
            head: head node of linked list.
        Returns:
            length of linked list.
        """
        length = 0
        current = head
        while current is not None:
            length += 1
            current = current.next
        return length
    


node1 = ListNode(4)
node2 = ListNode(1)
node3 = ListNode(8)
node4 = ListNode(4)
node5 = ListNode(5)

node6 = ListNode(5)
node7 = ListNode(6)
node8 = ListNode(1)

#connect the nodes for ListA
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

#connect the nodes for ListB
node6.next = node7
node7.next = node8
node8.next = node3

sol = Solution()

intersection_node = sol.getIntersectionNode(node1, node6)

if intersection_node is not None:
    print("Intersected at node with value: ", intersection_node.val)
else:
    print("No intersection found.")