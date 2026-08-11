class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def traverse(self, target):
        current = self.head
        while current is not None:
            if current.value == target:
                return True
            current = current.next
        return False


dll= DoublyLinkedList()

dll.head = Node("A")
dll.head.next = Node("B")
dll.head.next.prev = dll.head
dll.head.next.next = Node("C")
dll.head.next.next.prev = dll.head.next

dll.tail = dll.head.next.next

print(dll.traverse("B"))


