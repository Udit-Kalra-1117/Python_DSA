class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def print_nodes_at_distance_k(node, k):
    # checking if the current node has any children
    if node is None:
        return
    # checking if the required distance is traversed or not
    if k == 0:
        print(node.data, end=" ")
    else:
        # if the required distance is not traversed then continue to traverse to the left an right children till required
        print_nodes_at_distance_k(node.left, k-1)
        print_nodes_at_distance_k(node.right, k-1)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
k = 2
print("Items at distance",k,"in the given tree are:", end=" ")
print_nodes_at_distance_k(root, k)
print()