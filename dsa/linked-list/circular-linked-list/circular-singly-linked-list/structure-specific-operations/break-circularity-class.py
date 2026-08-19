class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def traverse(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        while True:
            print(current.value, end=" -> ")
            current = current.next

            if current == self.head:
                print("(back to head)")
                break

    def break_circularity(self):
        if self.head is None:
            return
        self.tail.next = None



csll = CircularSinglyLinkedList()

csll.node_a = Node("A")
csll.node_b = Node("B")
csll.node_c = Node("C")
csll.node_d = Node("D")

# Set head and tail
csll.head = csll.node_a
csll.tail = csll.node_d

# Connect nodes
csll.node_a.next = csll.node_b
csll.node_b.next = csll.node_c
csll.node_c.next = csll.node_d

# Create circular link
csll.node_d.next = csll.node_a

# Traverse circular list
csll.traverse()

# Break circularity
csll.break_circularity()

# Traverse normal linked list
current = csll.head

while current is not None:
    print(current.value, end=" -> ")
    current = current.next

print("None")