class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

# a function to do in-order traversal
def inorder_traversal(root):
    if root:
        # recurring on the left child
        inorder_traversal(root.left)
        # printing the value of the left child
        print(root.value, end=" ")
        # recurring on the right child
        inorder_traversal(root.right)

# a function to do pre-order traversal
def preorder_traversal(root):
    if root:
        # printing the value of current node first
        print(root.value, end=" ")
        # recurring on the left child
        preorder_traversal(root.left)
        # recurring on the right child
        preorder_traversal(root.right)

# a function to do post-order traversal
def postorder_traversal(root):
    if root:
        # recurring on the left child
        postorder_traversal(root.left)
        # recurring on the right child
        postorder_traversal(root.right)
        # printing the value of the left node
        print(root.value, end=" ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Pre-order: ", end=" ") 
preorder_traversal(root)
print("\nPost-order: ", end=" ") 
postorder_traversal(root)
print("\nIn-order: ", end=" ") 
inorder_traversal(root)
print()