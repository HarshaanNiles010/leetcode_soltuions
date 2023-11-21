# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #curr = list1
        #while curr != None:
        #    print(curr.val)
        #    curr = curr.next
        returnList = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                # Add to the return linked list
                node.next = list1
                list1 = list1.next
            else:
                # Add to the return linked list
                node.next = list2
                list2 = list2.next
            # update the pointer to the next for the node
            node = node.next
        node.next = list1 or list2
        return returnList.next