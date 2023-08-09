class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def insert_value(root, value):
    # checking if the root node is there or not if not then making it
    if root is None:
        return Node(value)

    # checking if the current node's value is less than the value to be inserted,
    # if yes then adding it in the right subtree
    elif root.data < value:
        root.right = insert_value(root.right, value)

    # checking if the current node's value is greater than the value to be inserted,
    # if yes then adding it in the left subtree
    else:
        root.left = insert_value(root.left, value)

    # returning the created node
    return root

def inorder_traversal(node):
    if node:
        # recurring on the left child
        inorder_traversal(node.left)
        # printing the value of the left child
        print(node.data, end=" ")
        # recurring on the right child
        inorder_traversal(node.right)

# driver code
root = Node(70)
# root - None
# root = insert_value(root, 70)
root = insert_value(root, 50)
root = insert_value(root, 90)
root = insert_value(root, 30)
root = insert_value(root, 60)
root = insert_value(root, 80)
root = insert_value(root, 110)
inorder_traversal(root)
print()