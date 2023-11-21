class Node:
    def __init__(self, val = 0, next_node = None):
        self.val = val
        self.next_node = next_node
    
class Linked_List:
    def __init__(self):
        self.head = None
        
    def linked_list_length(self):
        length = 0
        if self.head is None:
            return length
        current_node = self.head
        while current_node.next_node:
            length += 1
            current_node = current_node.next_node
        return length
    
    def insert_at_start(self, val):
        temp_node = Node(val)
        if self.head is None:
            self.head = temp_node
            return
        else:
            temp_node.next_node = self.head
            self.head = temp_node
    
    def insert_at_end(self, val):
        temp_node = Node(val)
        if self.head is None:
            self.head = temp_node
            return
        
        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = temp_node 
    
    def insert_at_position(self, val, position):
        if position < 0:
            raise Exception("Invalid position less than the length of the list")
        if position > self.linked_list_length():
            raise Exception("Invalid position greater than the length of the list")
        temp_node = Node(val)
        current_node = self.head
        current_position = 0
        if current_position == position:
            if self.head is None:
                self.head = temp_node
                return
            temp_node.next_node = self.head
            self.head = temp_node
        while(current_node != None and current_position + 1 != position):
            current_position += 1
            current_node = current_node.next_node
            if current_node != None:
                temp_node.next_node = current_node.next_node
                current_node.next_node = temp_node
            else:
                raise Exception("Index not available")

    def print_linked_list(self):
        current_node = self.head
        while current_node:
            print(current_node.val, end="->")
            current_node = current_node.next_node
        print("None")
    
    def remove_at_head(self):
        if self.head == None:
            return
        self.head = self.head.next_node

    def remove_at_end(self):
        if self.head == None:
            return
        current_node = self.head
        while current_node.next_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = None
    
    def remove_at_index(self, index):
        
        if self.head == None:
            return 
        
        current_node = self.head
        current_position = 0
        if current_position == index:
            if self.head == None:
                return
            self.head = self.head.next_node
        while (current_node != None and current_position +1 != index):
            current_position += 1
            current_node = current_node.next_node
            if current_node != None:
                current_node.next_node = current_node.next_node.next_node
            else:
                raise Exception("Index is not present")
        
    def search_linked_list(self, target):
        if self.head == None:
            return -1
        current_node = self.head
        current_position = 0
        while current_node:
            if current_node.val == target:
                return current_position
            current_node = current_node.next_node
            current_position += 1
        
if __name__ == '__main__':
    l1 = Linked_List()
    arr = [(i) for i in range(10)]
    print(arr)
    for a in arr:
        l1.insert_at_end(a)
    l1.print_linked_list()
    l1.insert_at_position(45,2)
    l1.print_linked_list()
    l1.remove_at_end()
    l1.print_linked_list()
    l1.remove_at_head()
    l1.print_linked_list()
    print(l1.search_linked_list(45))
    