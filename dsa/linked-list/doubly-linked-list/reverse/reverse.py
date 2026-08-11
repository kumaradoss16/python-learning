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

        while current:
            print(current.value, end=" <-> ")
            current = current.next

        print("None")

    def reverse(self):
        current = self.head
        while current:
            current.next, current.prev = current.prev, current.next

            current = current.prev

        self.head, self.tail = self.tail, self.head


dll = DoublyLinkedList()
dll.head = Node("A")
dll.head.next = Node("B")
dll.head.next.prev = dll.head
dll.head.next.next = Node("C")
dll.head.next.next.prev = dll.head.next

dll.tail = dll.head.next.next

print("Before Reverse:")
dll.traverse()

dll.reverse()
print("After Reverse:")
dll.traverse()