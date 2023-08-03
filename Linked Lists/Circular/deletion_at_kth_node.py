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

        # if there is a linked list already present then
        # add element just after the head node and
        # swapping the values of the new_node and the head node
        new_node.next = self.head.next
        self.head.next = new_node
        self.head.data, new_node.data = new_node.data, self.head.data

    def delete_start(self):
        # if there is only one node present
        if self.head.next == self.head:
            print("Node deleted: ", self.head.data)
            self.head = None
            return

        print("Node deleted: ", self.head.data)
        self.head.data = self.head.next.data
        self.head.next = self.head.next.next

    def delete_node(self, k):
        if self.head == None:
            print("Linked List is already empty, nothing to delete")
            return
        if k == 1:
            self.delete_start()
            return
        
        current = self.head
        for i in range(k-2):
            current = current.next
        print("Node deleted: ", current.next.data)
        current.next = current.next.next


    def display(self):
        temp = self.head

        if temp == None:
            print("Linked List is empty nothing to print")
            return
        
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break

#Drive Code
ll = LinkedList () 

ll.insert (12) 
ll.insert (16) 
ll.insert (20) 

ll.insert (24) 
ll.insert (30) 
ll.insert (22) 
print()
ll.display () 
print () 

#3rd node
print()
ll.delete_node(3) 
ll.display () 
print()

#last node
print()
ll.delete_node (5) 
ll.display () 
print()

#first node
print()
ll.delete_node (1) 
ll.display () 
print()

#second node
print()
ll.delete_node (2) 
ll.display () 
print()

#first node
print()
ll.delete_node (1) 
ll.display () 
print()

#first node
print()
ll.delete_node (1) 
ll.display () 
print()
ll.display ()
print()