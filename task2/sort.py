class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # Traverse preorder
    def RootLeftRight(self):
        print(self.val, end=' ')
        if self.left:
            self.left.RootLeftRight()
        if self.right:
            self.right.RootLeftRight()

    # Traverse inorder
    def LeftRootRight(self):
        if self.left:
            self.left.LeftRootRight()
        print(self.val, end=' ')
        if self.right:
            self.right.LeftRootRight()

    # Traverse postorder
    def LeftRightRoot(self):
        if self.left:
            self.left.LeftRightRoot()
        if self.right:
            self.right.LeftRightRoot()
        print(self.val, end=' ')


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)

print("Pre order Traversal: ", end="")
root.RootLeftRight()
print("\nIn order Traversal: ", end="")
root.LeftRootRight()
print("\nPost order Traversal: ", end="")
root.LeftRightRoot()