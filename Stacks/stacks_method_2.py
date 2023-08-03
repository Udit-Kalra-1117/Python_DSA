# This is used to return -infinite whenever our stack is empty
from sys import maxsize


class Stack:
    def __init__(self):
        self.stack = []

    # If your length of stack is 0 then stack is empty
    def isEmpty(self):
        return len(self.stack) == 0

    # Just use append to add item
    def push(self, item):
        self.stack.append(item)
        print(item + " pushed to stack ")

    # Pop removes the top most / last element in stack/list
    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
            return str(-maxsize - 1)  # return minus infinite

        return self.stack.pop()

    # Get the topmost element in the stack
    def peek(self):
        if self.isEmpty():
            return str(-maxsize - 1)  # return minus infinite
        return self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)

    def display(self):
        # writing extra ways to practise ways of writing the same in python
        print(" ".join(x for x in self.stack))  # will not print in top to bottom format
        print(" ".join(self.stack[i] for i in range(len(self.stack))))  # will not print in top to bottom format
        print(" ".join(self.stack[i] for i in range(len(self.stack)-1, -1, -1)))  # Will print in top to bottom format (Correct)
        print(" ".join(item for item in self.stack[::-1]))  # will print in top to bottom format (Correct)
        print(", ".join(item for item in self.stack[::-1]))  # will print in top to bottom format (Correct)


# Driver program
s = Stack()
s.push(str(5))
s.push(str(10))
s.push(str(15))
s.push(str(20))
print(s.pop() + " popped from stack")
print(s.peek() + " is top of the stack")
print(str(s.size()) + " is size of stack")
s.display()