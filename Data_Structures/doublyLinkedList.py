class ListNode:
    def __init__(self, val = 0, next_ptr = None, prev_ptr = None):
        self.val = val
        self.next_ptr = next_ptr
        self.prev_ptr = prev_ptr
    

class Doubly_Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def linked_list_length(self):
        current_node = self.head
        length = 0
        if self.head == None:
            return length
        while current_node:
            length += 1
            current_node = current_node.next_ptr
        return length    

    def print_doubly_linked_list(self):
        current_node = self.head
        print("head", end="<=>")
        while current_node:
            print(current_node.val, end='<=>')
            current_node = current_node.next_ptr
        print("tail")

    def insert_at_start(self, val):
        temp_node = ListNode(val)
        temp_node.next_ptr = self.head
        if self.head != None:
            self.head.prev_ptr = temp_node
            self.head = temp_node
            temp_node.prev_ptr = None
        else:
            self.head = temp_node
            self.tail = temp_node
            temp_node.prev_ptr = None
    
    def insert_at_end(self, val):
        temp_node = ListNode(val)
        temp_node.prev_ptr = self.tail
        if self.tail == None:
            self.head = temp_node
            self.tail = temp_node
            temp_node.next_ptr = None
        else:
            self.tail.next_ptr = temp_node
            temp_node.next_ptr = None
            self.tail = temp_node
    
    
    def insert_at_position(self, val, position):
        if position < 0:
            raise Exception("Invalid position less than the length of the list")
        if position > self.linked_list_length():
            raise Exception("Invalid position, position greater than the length of the list")
        current_node = self.head
        current_position = 0
        temp_node = ListNode(val)
        if current_position == position:
            temp_node.next_ptr = self.head
            if self.head != None:
                self.head.prev_ptr = temp_node
                self.head = temp_node
                temp_node.prev_ptr = None
            else:
                self.head = temp_node
                self.tail = temp_node
                temp_node.prev_ptr = None
        else:
            while current_node != None and current_position + 1 != position:
                current_position += 1
                current_node = current_node.next_ptr
                if current_node != None:
                    temp_node.next_ptr = current_node
                    current_node.next_ptr = temp_node
                    temp_node.prev_ptr = current_node
                    if current_node.next_ptr is not None:
                        current_node.next_ptr.prev_ptr = temp_node
                else:
                    raise Exception("Index not available")
                

if __name__ == '__main__':
    d1 = Doubly_Linked_list()
    arr = [i for i in range(10)]
    for a in arr:
        d1.insert_at_end(a)
    d1.print_doubly_linked_list()
    d1.insert_at_position(466,2)
    d1.print_doubly_linked_list()