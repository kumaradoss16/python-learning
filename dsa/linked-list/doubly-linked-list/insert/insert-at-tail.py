class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

    def insert_at_tail(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node


dll = DoublyLinkedList()

dll.head = Node("A")

dll.head.next = Node("B")
dll.head.next.prev = dll.head

dll.head.next.next = Node("C")
dll.head.next.next.prev = dll.head.next
dll.tail = dll.head.next.next
print("Before Inserting a value at a tail in the DLL: ")
dll.traverse()

dll.insert_at_tail("X")
print("After Insert a value at a tail in the DLL: ")
dll.traverse()
