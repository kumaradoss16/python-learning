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

    def delete_node(self, node):
        if node is None:
            return False

        if node == self.head:
            self.head = node.next

        if node == self.tail:
            self.tail = node.prev

        if node.prev is not None:
            node.prev.next = node.next

        if node.next is not None:
            node.next.prev = node.prev

        node.prev = None
        node.next = None

        return True

dll= DoublyLinkedList()

dll.head = Node("A")
dll.head.next = Node("B")
dll.head.next.prev = dll.head
dll.head.next.next = Node("C")
dll.head.next.next.prev = dll.head.next

dll.tail = dll.head.next.next

print("Before deletion:")
dll.traverse()

# Delete node X
dll.delete_node(dll.head.next)

print("After deletion:")
dll.traverse()
