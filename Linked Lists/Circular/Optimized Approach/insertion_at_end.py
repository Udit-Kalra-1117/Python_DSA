class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        # checking if there is a node present in the linked list
        if self.head == None:
            self.head = new_node
            new_node.next = new_node
            return

        # if there is a linked list already present then
        # add element just after the head node and
        # swapping the values of the new_node and the head node
        # lastly pushing the head node one place ahead so as the newly inserted node is inserted at the last
        new_node.next = self.head.next
        self.head.next = new_node
        self.head.data, new_node.data = new_node.data, self.head.data
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
ll.insert(22)
ll.insert(30)
ll.insert(24)

print()
ll.display()
print()