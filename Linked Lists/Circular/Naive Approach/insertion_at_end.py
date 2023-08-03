class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        # checking if there is a linked list already present
        if self.head == None:
            self.head = new_node
            new_node.next = new_node
            return
        
        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def display(self):
        temp = self.head
        if temp == None:
            print("Linked List is empty there is nothing to print")
            return
        
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break

# driver code
ll = LinkedList()

ll.insert(12)
ll.insert(16)
ll.insert(20)
ll.insert(24)
ll.insert(30)
ll.insert(22)

print()
ll.display()
print()