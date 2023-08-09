class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def size_of_tree(root):
    if root is None:
        return 0
    # initializing a queue and adding current node to it
    queue = []
    queue.append(root)
    # initializing a count variable
    count = 0

    while len(queue) > 0:
        # incrementing count for each new node
        count += 1
        node = queue.pop(0)

        # checking for the left children
        if node.left is not None:
            queue.append(node.left)

        # checking for the right children
        if node.right is not None:
            queue.append(node.right)

    return count

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.right.right.left = Node(7)
root.right.right.right = Node(8)

print("The level order traversal of the given tree is: ", size_of_tree(root))