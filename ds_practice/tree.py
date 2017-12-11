class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert_left(self, child):
        if self.left is None:
            self.left = child
        else:
            child.left = self.left
            self.left = child
    
    def insert_right(self, child):
        if self.right is None:
            self.right = child
        else:
            child.right = self.right
            self.right = child

def main():
    root = Node(1)
    root.insert_left(Node(2))
    assert root.left.val == 2
    root.insert_left(Node(3))
    assert root.left.val == 3
    assert root.left.left.val == 2

if __name__ == "__main__":
    main()