# a binary search tree has all unique valued nodes i.e. no node has same value
# a binary search tree always has a higher valued node than itself as its right child and a lower valued node than itself as its left child

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

def search_item(root, value):
    # checking if the root is present or not or the root value is the required value or not
    if root is None or root.data == value:
        return root

    # checking if the current root's value is less than the required value then searching through the right subtree
    if root.data < value:
        return search_item(root.right, value)

    # if none of the above statements satisfy then required value is lesser than the current node's value so search through the left subtree
    return search_item(root.left, value)

# driver code
root = Node(70)
# root = None
# root = insert_value(root, 70)
root = insert_value(root, 50)
root = insert_value(root, 90)
root = insert_value(root, 30)
root = insert_value(root, 60)
root = insert_value(root, 80)
root = insert_value(root, 110)
key = int(input("Enter the node value to be searched: "))
if search_item(root, key) is None:
    print(key,"is not present in the given tree")
else:
    print(key,"is found in the given tree")