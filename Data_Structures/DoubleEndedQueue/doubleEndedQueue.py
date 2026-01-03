class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Deque:

    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.tail.prev = self.head # type: ignore
        self.head.next = self.tail # type: ignore

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        temp = Node(value)
        last_node = self.tail.prev
        last_node.next = temp # type: ignore
        temp.prev = last_node
        temp.next = self.tail # type: ignore
        self.tail.prev = temp # type: ignore

    def appendleft(self, value: int) -> None:
        temp = Node(value)
        first_node = self.head.next
        self.head.next = temp # type: ignore
        temp.prev = self.head # type: ignore
        first_node.prev = temp # type: ignore
        temp.next = first_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last_node = self.tail.prev
        value = last_node.data # type: ignore
        prev_node = last_node.prev # type: ignore
        prev_node.next = self.tail
        self.tail.prev = prev_node
        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        first_node = self.head.next
        value = first_node.data # type: ignore
        second_node = first_node.next # type: ignore
        self.head.next = second_node
        second_node.prev = self.head
        return value
