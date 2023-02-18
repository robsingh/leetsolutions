"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

The number of nodes in each linked list is in the range [1, 100].
It is guaranteed that the list represents a number that does not have leading zeros.

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        # Initialize a dummy node to keep track of the head of resultant linked list
        dummy = ListNode()
        # Initialize a pointer to keep track of head of the resultant linked list
        current = dummy
        # Initialize a variable to keep track of the carry
        carry = 0

        # Iterate through the Linked Lists until both are exhausted
        while l1 or l2 or carry:
            # Get the values of the current digits in the Linked List, or 0 if it is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the carry and the value of the current digit in linked list
            carry,val = divmod(val1 + val2 + carry, 10)

            # create a new node in the resultant linked lst with calculated values
            current.next = ListNode(val)

            # Move the pointer to the next node in the resultant linked list
            current = current.next

            # Move the pointers to the next node in input linked lists, if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the next node of the dummy node, which is the head of the resultant linked list
        return dummy.next


