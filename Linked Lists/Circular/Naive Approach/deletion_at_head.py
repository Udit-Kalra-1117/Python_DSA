class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        # checking if the node to be inserted is the first node of the linked list
        if self.head == None:
            self.head = new_node
            new_node.next = new_node
            return
        
        # if there is a linked list already present then
        # add element just after the head node and
        # swapping the values of the new_node and the head node
        new_node.next = self.head.next
        self.head.next = new_node
        self.head.data, new_node.data = new_node.data, self.head.data

    def delete_start(self):
        # if the linked list is empty
        if self.head == None:
            print("Linked List is empty there is nothing to delete")
            return
        
        # if there is only one node present
        if self.head.next == self.head:
            print("Node deleted: ", self.head.data)
            self.head = None
            return
        
        # traverse to the last node to delete it
        current = self.head
        while current.next != self.head:
            current = current.next
        
        current.next = self.head.next
        print("Node deleted: ", self.head.data)
        self.head = self.head.next

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
ll.insert(30)
ll.insert(24)
ll.insert(22)

print()
ll.display()
print()

print()
ll.delete_start()
ll.display()
print()
print()
ll.delete_start()
ll.display()
print()
print()
ll.delete_start()
ll.display()
print()
print()
ll.delete_start()
ll.display()
print()
print()
ll.delete_start()
ll.display()
print()
print()
ll.delete_start()
ll.display()
print()