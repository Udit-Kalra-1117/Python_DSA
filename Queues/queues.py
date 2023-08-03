class Queue:
    def __init__(self, cap):
        self.queue = [None] * cap
        self.front = None
        self.rear = None
        self.capacity = cap

    def is_full(self):
        if self.rear == self.capacity - 1:
            print("Overflow condition, can't Enqueue more elements!!")
        
        return self.rear == self.capacity - 1

    def is_empty(self):
        if self.front is None:
            print("Underflow condition, can't Dequeue more elements!!")
        
        return self.front is None

    def enqueue(self, item):
        if self.is_full():
            return
        
        if self.front is None:
            self.front = 0
            self.rear = 0
        else:
            self.rear += 1
        
        self.queue[self.rear] = item
        print(self.queue[self.rear], " enqueued to queue!")

    def dequeue(self):
        if self.is_empty():
            return
        
        item = self.queue[self.front]
        self.front += 1

        # resetting the queue when the last item is dequeued
        if self.front > self.rear:
            self.front = self.rear = None
        
        print(item, " dequeued from the queue!!")

    def display(self):
        if self.rear is None:
            print("Queue is already empty!!")
        else:
            i = self.front
            print("Queue: ", end = " ")

            while i <= self.rear:
                print(self.queue[i], end = " ")
                i += 1

# driver code
q = Queue(5)

print()
q.enqueue(10)
print()
q.display()
print()
q.enqueue(20)
print()
q.display()
print()
q.enqueue(30)
print()
q.display()
print()
q.enqueue(40)
print()
q.display()
print()
q.enqueue(50)
print()
q.display()
print()
print()
q.dequeue()
print()
q.display()
print()
q.dequeue()
print()
q.display()
print()