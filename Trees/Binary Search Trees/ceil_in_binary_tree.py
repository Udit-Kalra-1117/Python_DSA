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

def ceil_value(root, value):
    # checking if the root is there or not
    if root is None:
        return None

    # checking if the required ceil value is the value of the root itself
    if root.data == value:
        return root.data

    # if the root value is greater than the required ceil value then searching through the left subtree to find the ceil
    if root.data < value:
        return ceil_value(root.right, value)

    # if the ceil is still not found then search the right subtree
    ceilValue = ceil_value(root.left, value)
    if ceilValue is not None and ceilValue >= value:
        return ceilValue

    # if still not found then root value is the required float
    return root.data

# driver code
root = Node(70)
root = insert_value(root, 50)
root = insert_value(root, 90)
root = insert_value(root, 30)
root = insert_value(root, 60)
root = insert_value(root, 80)
root = insert_value(root, 110)
root = insert_value(root, 75)
root = insert_value(root, 65)
value = int(input("Enter the ceil value to find from the given tree: "))
print("The ceil value for",value,"form the given tree is:",ceil_value(root, value))