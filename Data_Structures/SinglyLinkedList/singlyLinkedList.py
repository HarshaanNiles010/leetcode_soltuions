from typing import List


class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while curr:
            if i == index: return curr.data
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        temp_node = ListNode(val)
        temp_node.next = self.head.next
        self.head.next = temp_node
        if not temp_node.next:
            self.tail = temp_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.data)
            curr = curr.next
        return res
