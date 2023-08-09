class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

def inorder_traversal(node):
    if node:
        # recurring on the left child
        inorder_traversal(node.left)

        # printing the value of the left child
        print(node.data, end=" ")

        # recurring on the right child
        inorder_traversal(node.right)

def inorder_successor(node):
    # in order to get the next higher value in the in-order traversal we switch to right branch of the tree
    # since the required value is higher so it will be towards the right subtree only
    node = node.right

    # now as the value is just consecutive higher value than the current node's value which is to be deleted
    # then it would be present in the left subtree now so traversing till the value is found
    while node is not None and node.left is not None:
        node = node.left
    return node

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

def delete_value(root, value):
    # checking if the tree is present or not
    if root is None:
        return None

    # checking if the value to be deleted is smaller than the current node's value then delving down the left subtree
    if root.data > value:
        root.left = delete_value(root.left, value)

    # checking if the value to be deleted is greater than the current node's value then delving down the right subtree
    elif root.data < value:
        root.right = delete_value(root.right, value)

    # the value at the current node is the value to be deleted
    else:

        # checking if the node that is going to be deleted has children or not
        # if the node has a right child only and not any left child 
        # then assigning the right child node in place of the node which is to be deleted
        # valid even if there is no right child as temp would have a value of NULL(NONE) only
        if root.left is None:
            temp = root.right
            del root
            return temp

        # if the node has a left child only and not any right child 
        # then assigning the left child node in place of the node which is to be deleted
        # valid even if there is no right child as temp would have a value of NULL(NONE) only
        elif root.right is None:
            temp = root.left
            del root
            return temp

        # checking if the root node is to be deleted then,
        # finding the minimum element from the right sub-tree and replacing its data with the root(parent) node's data
        else:
            successor_node = inorder_successor(root)

            # swapping values between nodes
            root.data = successor_node.data

            # deleting the node from the tree whose value is swapped with the root node
            # and maintaining the appropriate tree structure
            # root.right because the inorder successor would be in the right subtree only
            # and we would have to maintain the right subtree only as only that part would be modified
            root.right = delete_value(root.right, successor_node.data)
    return root

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

print("Original Binary Search Tree: ", end=" ")
inorder_traversal(root)

val1 = int(input("\n\nEnter the node value which you want to delete: "))
root = delete_value(root, val1) # trying to delete a leaf node: enter - any of 30, 65, 75, 110
print("\nModified Binary Search Tree after deleting node with value", val1,"is: ", end=" ")
inorder_traversal(root)

val2 = int(input("\n\nEnter the node value which you want to delete: "))
root = delete_value(root, val2) # trying to delete a node having single child: enter - any of 60, 80
print("\nModified Binary Search Tree after deleting node with value", val2,"is: ",end=" ")
inorder_traversal(root)

val3 = int(input("\n\nEnter the node value which you want to delete: "))
root = delete_value(root, val3) # trying to delete a node with both left and right children: enter - any of 70, 50, 90
print("\nModified Binary Search Tree after deleting node with value", val3,"is: ",end=" ")
inorder_traversal(root)

val4 = int(input("\n\nEnter the node value which you want to delete: "))
root = delete_value(root, val4) # trying to delete a root node: enter - 70
print("\nModified Binary Search Tree after deleting node with value", val4,"is: ",end=" ")
inorder_traversal(root)
print()