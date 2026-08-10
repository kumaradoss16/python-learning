class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")



    def insert_at_head(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node


dll = DoublyLinkedList()

dll.head = Node("A")

dll.head.next = Node("B")
dll.head.next.prev = dll.head

dll.head.next.next = Node("C")
dll.head.next.next.prev = dll.head.next
print("Before Inserting a value at a head in the DLL: ")
dll.traverse()

dll.insert_at_head("X")
print("After Insert a value at a head in the DLL: ")
dll.traverse()



