class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

# function to get the path from a particular value passed
def get_path(root, path, value):
    # checking if the root node is present or not or if the leaf node is reached or not
    if root is None:
        return False

    # adding the root node to a path list
    path.append(root)

    # checking if the value to be found is traversed till or not
    if root.data == value:
        return True

    # if the required value is not reached then checking in the left child's subtree entirely first and right child's subtree next
    if get_path(root.left, path, value) or get_path(root.right, path, value):
        return True

    # if still not the required value is not reached after traversing the entire left subtree and right subtree then 
    # remove the lastly added node from the path list
    path.pop()
    return False

def get_least_common_ancestor(root, value1, value2):
    # defining two empty lists for defining paths for two different values (leaf nodes)
    path1 = []
    path2 = []

    # checking if the path exists or not for even any of the given leaf node from the root of the tree
    if get_path(root, path1, value1) == False or get_path(root, path2, value2) == False:
        return None

    # printing the paths if they exist
    print("\nPath for node with value",value1,"is:")
    [print(path1[i].data, end=" ") for i in range(len(path1))]

    print("\n\nPath for node with value",value2,"is:")
    [print(path2[i].data, end=" ") for i in range(len(path2))]

    # finding the common nodes for the both the obtained paths and printing the data value of the last common node
    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        i += 1

    # return the previous node in the path list as the value of i would be incremented before the loop ends
    return path1[i-1]
    # return path1[i-1].data

root = Node(70)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(50)
root.left.right = Node(10)
root.left.left.left = Node(60)
root.left.left.right = Node(40)
root.left.left.left.left = Node(90)
root.left.left.right.right = Node(110)
root.left.right.right = Node(80)
root.left.right.right.right = Node(100)

# print("\n\nThe Least Common Ancestor is:",get_least_common_ancestor(root, 90, 110))
print("\n\nThe Least Common Ancestor is:",get_least_common_ancestor(root, 90, 110).data)