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

    def update_at_index(self, index, new_value):
        current = self.head
        current_index = 0

        while current:
            if current_index == index:
                current.value = new_value
                return True
            current = current.next
            current_index += 1
        return False


dll= DoublyLinkedList()

dll.head = Node("A")
dll.head.next = Node("B")
dll.head.next.prev = dll.head
dll.head.next.next = Node("C")
dll.head.next.next.prev = dll.head.next

print("Before Update:")
dll.traverse()

dll.update_at_index(1, "X")
print("After Update:")
dll.traverse()
