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

    def delete_head(self):
        if self.head is None:
            return
        # Move head to the second node
        new_head = self.head.next

        # List became empty
        if new_head is not None:
            new_head.prev = None

        self.head = new_head


dll = DoublyLinkedList()
dll.head = Node("A")
dll.head.next = Node("B")
dll.head.next.prev = dll.head
dll.head.next.next = Node("C")
dll.head.next.next.prev = dll.head.next


dll.delete_head()
dll.traverse()