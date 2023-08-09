class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def size_of_tree(root):
    if root is None:
        # checking if the leaf node is reached or not
        return 0
    else:
        # traversing to all the nodes of the tree
        return 1 + size_of_tree(root.left) + size_of_tree(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.right.right.left = Node(7)
root.right.right.right = Node(8)

print("The size of the given tree is: ", size_of_tree(root))