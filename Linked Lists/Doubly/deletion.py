class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head

        # if linked list already has 1 node
        if self.head != None:
            self.head.prev = new_node
        # changing the head to freshly created node
        self.head = new_node

    def delete_node(self, value):
        temp = self.head
        previous = None

        # case when there is only 1 node in the list
        if temp.next == None:
            self.head = None
            print("\nValue deleted:", temp.data)
            return

        # if the head node itself is to be deleted
        if temp != None and temp.data == value:
            self.head = temp.next
            self.head.prev = None
            print("\nValue deleted:", temp.data)
            return

        # run through the linked list until we find the value
        while temp != None and temp.data != value:
            previous = temp
            temp = temp.next

        if temp == None:
            print("\nValue not found")
            return

        previous.next = temp.next

        # if the last node is to be deleted
        if temp.next == None:
            print("\nValue deleted:", temp.data)
            return

        temp.next.prev = previous
        print("\nValue deleted:", temp.data)

    def display(self):
        temp = self.head
        end = None
        print("\nLinked in forward direction:")
        while temp:
            print(temp.data, end=" ")
            end = temp
            temp = temp.next
        print("")
        print("\nLinked list in backward direction:")
        while end:
            print(end.data, end=" ")
            end = end.prev
        print("")

# Drive Code
ll = LinkedList()

ll.insert(12)
ll.insert(16)
ll.insert(20)
ll.insert(24)
ll.insert(30)
ll.insert(22)

ll.display()

# deleting first occurrence of a value in linked list
ll.delete_node(22)
ll.display()

ll.delete_node(20)
ll.display()

ll.delete_node(12)
ll.display()

ll.delete_node(30)
ll.display()

ll.delete_node(16)
ll.display()

ll.delete_node(24)
ll.display()
