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

    def delete_tail(self):
        if self.tail is None:
            return
        # Move head to the second node
        new_tail = self.tail.prev

        # List became empty
        if new_tail is not None:
            new_tail.next = None

        self.tail = new_tail


dll = DoublyLinkedList()
dll.head = Node("A")
dll.head.next = Node("B")
dll.head.next.prev = dll.head
dll.head.next.next = Node("C")
dll.head.next.next.prev = dll.head.next

dll.tail = dll.head.next.next


dll.delete_tail()
dll.traverse()