"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the 
first two lists.
Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0] 
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        """
        Merge two sorted linked lists into a single sorted linked list.

        Args:
        list1 (ListNode): Head node of the first linked list.
        list2 (ListNode): Head node of the second linked list.
        
        Returns:
        ListNode: Head node of the merged linked list.
        """

        dummy = ListNode(0)  # creating a dummy node to use as the head of the merged list
        tail = dummy # tail node to keep track of end of the merged list

        # if the value of the node in list1 is smaller, link the current node to the end of the merged list
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next  # move the tail node to the end of the merged list

        #link the remaining nodes in list1 or list2, if any to the end of merged list
        tail.next = list1 or list2

        return dummy.next

# create two linked lists for testing
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

sol = Solution()
merged_list = sol.mergeTwoLists(list1, list2)

# print values of the node in the merged list
current_node = merged_list
while current_node:
    print(current_node.val)
    current_node = current_node.next




        