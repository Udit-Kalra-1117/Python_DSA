class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

# defining a global variable called max_diameter to 0
max_diameter = 0

def height(root):
    if root is None:
        return 0
    # left_child_height = height(root.left)
    # right_child_height = height(root.right)

    # calculating the value of max_diameter along with the height of the tree in the same recursive call
    global max_diameter
    max_diameter = max(max_diameter, 1 + height(root.left) + height(root.right))
    # max_diameter = max(max_diameter, 1 + left_child_height + right_child_height)

    return 1 + max(height(root.left), height(root.right))
    # return 1 + max(left_child_height,right_child_height)

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

print("The height of the given tree is: ", height(root))
print("The diameter of the given tree is: ", max_diameter)