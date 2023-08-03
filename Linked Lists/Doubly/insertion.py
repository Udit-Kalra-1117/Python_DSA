class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_start(self, data):
        new_node = Node(data)
        new_node.next = self.head

        # if linked list already has start node
        if self.head != None:
            self.head.prev = new_node

        # change head to newly inserted node
        self.head = new_node

    def insert_last(self, data):
        new_node = Node(data)
        new_node.next = None

        #checking if there is no node present in linked list at all
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def display(self):
        temp = self.head
        end = None
        print("\nLinked List in forward direction: ")
        while temp:
            print(temp.data, end=" ")
            end = temp
            temp = temp.next
        print("")
        print("\nLinked List in backward direction: ")
        while end:
            print(end.data, end=" ")
            end = end.prev
        print("")

#Drive Code
ll = LinkedList() 

ll.insert_start (12) 
ll.insert_start (16) 
ll.insert_start (20) 
ll.insert_last (10) 
ll.insert_last (14) 
ll.insert_last (18) 
ll.insert_last (11) 

ll.display ()