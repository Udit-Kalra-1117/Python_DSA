# defining value of infinity
INFINITY = 9999999999

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key

def highest_node(root):
    if root is None:
        return -INFINITY
    else:
        return max(root.data, max(highest_node(root.left), highest_node(root.right)))

root = Node(20)
root.left = Node(70)
root.right = Node(90)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(60)
root.right.right.left = Node(30)
root.right.right.right = Node(80)

print("The highest node of the given tree is: ", highest_node(root))