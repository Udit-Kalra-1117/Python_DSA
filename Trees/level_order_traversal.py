class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def level_order_traversal(root):
    if root is None:
        return
    # initializing a queue and adding current node to it
    queue = []
    queue.append(root)

    while len(queue) > 0:
        # printing the value of current node
        print(queue[0].data, end=" ")
        node = queue.pop(0)

        # checking for the left children
        if node.left is not None:
            queue.append(node.left)

        # checking for the right children
        if node.right is not None:
            queue.append(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.right.right.left = Node(7)
root.right.right.right = Node(8)

print("The level order traversal of the given tree is: ")
level_order_traversal(root)
print()
