class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def spiral_level_order_using_two_stacks(root):
    if root is None:
        return

    # initializing two empty stacks
    stack1 = []
    stack2 = []

    # appending the current node to a stack
    stack1.append(root)

    # checking if the stacks are empty or not
    while len(stack1) != 0 or len(stack2) != 0:
        # checking if the stack1 is empty or not
        while len(stack1) != 0:
            # printing the top (last) value form the stack
            temp = stack1.pop()
            print(temp.data, end=" ")
            # adding left and right children in stack2
            if temp.left is not None:
                stack2.append(temp.left)
            if temp.right is not None:
                stack2.append(temp.right)
        print()

        # checking if the stack2 is empty or not
        while len(stack2) != 0:
            # printing the top (last) value from the stack
            temp = stack2.pop()
            print(temp.data, end=" ")
            # adding the right and left children in stack1
            if temp.right is not None:
                stack1.append(temp.right)
            if temp.left is not None:
                stack1.append(temp.left)
        print()

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
spiral_level_order_using_two_stacks(root)