class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def left_view(root):
    if root is None:
        return

    queue = []
    queue.append(root)

    # running till the queue is empty
    while queue:
        for i in range(len(queue)):
            # assigning the starting value of the queue to the temp variable
            temp = queue[0]
            queue.pop(0)
            # printing only the node's value which would be visible from the left view
            if i == 0:
                print(temp.data, end=" ")
            # adding the left and right children to the queue
            if temp.left is not None:
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)

root = Node(20)
root.left = Node(70)
root.right = Node(90)
root.left.left = Node(30)
root.left.right = Node(40)
root.right.right = Node(70)

print("The left view of the given tree includes the nodes: ",end="")
left_view(root)
print()