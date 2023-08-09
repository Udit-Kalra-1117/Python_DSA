class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def max_height(node):
    if node is None:
        return 0
    else:
        # Recur & calculate the Height of each (Left/ right) subtree
        left_height = max_height(node.left)
        right_height = max_height(node.right)
        # find the larger value and return it
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print("Maximum height of the tree is:",max_height(root))