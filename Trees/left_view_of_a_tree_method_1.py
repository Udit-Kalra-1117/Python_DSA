class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

# initializing the starting level and root to start the traversal
def print_left_view_helper(root):
    max_level_visited = [0]
    print_left_view(root, max_level_visited, 1)

def print_left_view(node, max_level_visited, current_level):
    if node is None:
        return
    # checking if the max level visited is less than the current level and if so then printing the node value
    if max_level_visited[0] < current_level:
        print(node.data, end=" ")
        max_level_visited[0] = current_level

    # traversing to the left and right children of the next level to print the left view
    print_left_view(node.left, max_level_visited, current_level + 1)
    print_left_view(node.right, max_level_visited, current_level + 1)

root = Node(20)
root.left = Node(70)
root.right = Node(90)
root.left.left = Node(30)
root.left.right = Node(40)
root.right.right = Node(70)

print("The left view of the given tree includes the nodes: ", end="")
print_left_view_helper(root)
print()

# In the given code, `max_level_visited` is used as a list to achieve a form of pass-by-reference behavior.
# This is a common technique in Python to modify variables within functions and retain the changes outside the function.
# In Python, when you pass a variable as an argument to a function, it's actually 
# passing a reference to the memory location of that variable.
# When you modify the variable inside the function, it's modifying the value at that memory location,
# and the changes will be visible outside the function as well. 
# However, when you reassign the variable inside the function to a new value, 
# it will create a new local variable with the same name, and the original variable outside the function remains unaffected.
# By using a list (`max_level_visited`) as the argument, you are effectively using a mutable container. 
# When you modify the contents of the list (e.g., `max_level_visited[0] = current_level`), 
# the changes are reflected outside the function as well, because the memory location of the list remains the same.
# If you were to use an integer variable instead of a list, like `max_level_visited = 0`, 
# any changes made to it within the `print_left_view` function would not be reflected outside the function. 
# This is because reassigning the integer variable inside the function would create a new local variable 
# instead of modifying the original variable outside the function.
# So, using a list in this context allows you to modify the value contained within the list 
# and have the changes visible outside the function. 
# It's a way to overcome the scoping limitations of variables within functions in Python.