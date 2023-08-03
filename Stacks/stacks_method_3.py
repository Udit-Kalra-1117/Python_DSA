stack = []

stack.append(100)
stack.append(200)
stack.append(300)

print(stack)

print(stack.pop())
print(stack.pop())

print(stack)
top=stack[-1]
print(top)
size=len(stack)
print(size)
print(stack.pop())


# removing comments from here print(stack.pop())
# Interpreter/compiler will throw an IndexError
# as the stack is  empty

# If the python list keeps on adding elements and becomes way too big
# then append() will take longer time because python will need to some memory allocation arrangements
# as the list items are stored in a contiguous way

# To solve the above deque methods can be used