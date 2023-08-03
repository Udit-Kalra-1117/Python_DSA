import math

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class My_Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        self.head = Node(data, self.head)

    def pop(self):
        if self.head is None:
            return math.inf
        k = self.head.data
        self.head = self.head.next
        return k

    def top(self):
        if self.head is None:
            return math.inf
        return self.head.data

s = My_Stack()
print()
print(s.pop())
s.push(10)
s.push(20)
print(s.pop())
print(s.pop())
print()