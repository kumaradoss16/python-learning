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

    def delete_by_value(self, target_value):
        current = self.head
        while current:
            if current.value == target_value:

                # Case 1: target is the head
                if current == self.head:
                    self.head = current.next

                    if self.head is not None:
                        self.head.prev = None
                    else:
                        self.tail = None

                # Case 2: target is the tail
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None

                # Case 3: target is in the middle
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                return True

            current = current.next
        return False


dll = DoublyLinkedList()

dll.head = Node("A")
dll.head.next = Node("B")
dll.head.next.prev = dll.head

dll.head.next.next = Node("C")
dll.head.next.next.prev = dll.head.next

dll.tail = dll.head.next.next

print("Before deletion: ")
dll.traverse()
dll.delete_by_value("B")

print("After deletion: ")
dll.traverse()

