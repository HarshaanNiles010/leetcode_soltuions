class Tree:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
    def insert(self, val):
        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = Tree(val)
                return
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = Tree(val)
                return
    
    def print_tree(self):
        if self.left:
            self.left.print_tree()
            print("<=",end="")
        print(self.val)
        if self.right:
            self.right.print_tree()
            print("=>",end="")


if __name__ == '__main__':
    t1 = Tree()
    for i in range(10):
        t1.insert(i)
    t1.print_tree()