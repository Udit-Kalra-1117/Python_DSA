# The diameter of a tree is the number of nodes on the longest path between two leaves in the tree.

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def height(root):
    if root is None:
        return 0
    else:
        return 1 + max(height(root.left), height(root.right))

def tree_diameter(root):
    if root is None:
        return 0
    parent_diameter = 1 + height(root.left) + height(root.right)
    left_child_diameter = tree_diameter(root.left)
    right_child_diameter = tree_diameter(root.right)

    return max(parent_diameter, max(left_child_diameter, right_child_diameter))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.left.right = Node(7)
root.left.right.right = Node(8)
root.left.left.left.left = Node(9)
root.left.right.right.right = Node(10)

print("The diameter of the given tree is: ", tree_diameter(root))