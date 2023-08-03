# List can become slow due to long length and append method may take longer time
# Deque is a better alternative since, deque provides O(1) time complexity at both ends
# that O(1) append or pop, while list has O(n) time complexity
from collections import deque

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)

print(stack)

top = stack[-1]
print(top)
size = len(stack)
print(size)


print(str(stack.pop()) + " Popped")
print(str(stack.pop()) + " Popped")
print(str(stack.pop()) + " Popped")
print(stack)

# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty