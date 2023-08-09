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
    # checking if the tree is present or not and even the case where the leaf node is traversed or not
    while root is not None:

        # checking if the required value is found in the tree
        if root.data == value:
            return True

        # if the required value is greater than the current node's value then search in the right subtree
        elif root.data < value:
            root = root.right

        # if the required value is smaller than the current node's value then search in the left subtree
        else:
            root = root.left

    # if the required value is not found in the entire tree then
    return False

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
if search_item(root, key):
    print(key,"is present in the given tree")
else:
    print(key,"is not found in the given tree")