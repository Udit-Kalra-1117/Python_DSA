class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key

def get_least_common_ancestor(root, value1, value2):
    # base case & case 4: none of the required node values are present so return none (null)
    if root is None:
        return None

    # case 1: if it is same as node 1 or node 2, we return current node as least common ancestor
    if root.data == value1 or root.data == value2:
        return root
    
    left_least_common_ancestor = get_least_common_ancestor(root.left, value1, value2)
    right_least_common_ancestor = get_least_common_ancestor(root.right, value1, value2)

    # case 2: if left subtree has one of the required value i.e. non-zero value 
    # and the right subtree has the other required value i.e. non-zero value 
    # then current node is the least common ancestor
    if left_least_common_ancestor and right_least_common_ancestor:
        return root

    # case 3: if its subtree has both the node then least common ancestor will also be in the subtree, 
    # check for least common ancestor in the below subtree
    return left_least_common_ancestor if left_least_common_ancestor is not None else right_least_common_ancestor

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
print("\nThe Least Common Ancestor is:",get_least_common_ancestor(root, 90, 110).data)