# this is used to return -infinity whenever the stack is empty
from sys import maxsize


# creating an empty stack
def create_stack():
    stack = []
    return stack

# if the length of stack is zero it is an empty stack
def is_empty(stack):
    return len(stack) == 0

# adding elements in the stack created earlier using append function
def push(stack, item):
    stack.append(item)
    print(item +" pushed into the stack")

# pop removes the top-most element in the stack or the last element from the list
def pop(stack):
    if(is_empty(stack)):
        print("Stack Underflow")
        return str(-maxsize - 1)
    return stack.pop()

def peek(stack):
    if(is_empty(stack)):
        return str(-maxsize - 1)
    return stack[-1]

stack = create_stack()
print("\nThe stack is: {}".format(stack))
print()
push(stack, str(5))
push(stack, str(10))
push(stack, str(15))
push(stack, str(20))
print("\nThe stack is: {}".format(stack))
print()
print(pop(stack) + " popped from the stack")
print(peek(stack) + " is the top most element in the stack")
print("\nThe stack is: {}".format(stack))
