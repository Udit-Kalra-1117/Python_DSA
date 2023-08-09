class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def spiral_level_order_helper(root):
    left_to_right = True
    spiral_level_order_using_one_stack(root, left_to_right)

def spiral_level_order_using_one_stack(root, left_to_right):
    if root is None:
        return 
    # initializing an empty queue and adding the element to it and and empty stack to store the node values to print it in spiral order
    queue = []
    queue.append(root)
    stack = []

    while len(queue) > 0:
        for _ in range(len(queue)):
            temp = queue[0]
            queue.pop(0)

            # if values are to be printed left to right print them right away
            if left_to_right:
                print(temp.data, end=" ")
            # else add them to the stack
            else:
                stack.append(temp)
            # adding left and right children
            if temp.left is not None:
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)

        # if the values are to be printed from right to left print the values from the stack in a reverse manner
        if not left_to_right:
            while len(stack) > 0:
                print(stack.pop().data, end=" ")

        print()
        # reverse the manner to print the values after printing each cycle (level)
        left_to_right = not left_to_right

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.left = Node(8)
root.right.left.right = Node(9)

print("\nEach node value of the given tree at each level in top to bottom manner is:")
spiral_level_order_helper(root)