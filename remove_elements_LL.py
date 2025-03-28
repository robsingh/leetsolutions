'''
Given the head of a linked list and an integer val, 
remove all the nodes of the linked list that has Node.val == val, and return the new head.

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Input: head = [], val = 1
Output: []
'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head:Optional[ListNode], val:int) -> Optional[ListNode]:
        # create a dummy node to simplify removal from the head of the list
        dummy = ListNode(next=head)
        current = dummy

        while current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current.next

        return dummy.next
    

#helper function to create a Linked List from a list
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


#helper function to convert a linked list to a list
def linked_list_to_list(head):
    lst = []
    current = head
    while current is not None:
        lst.append(current.val)
        current = current.next
    return lst


sol = Solution()
head = create_linked_list([1,2,3,6,5,4,7,6])
new_head = sol.removeElements(head, 6)
print(linked_list_to_list(new_head))

