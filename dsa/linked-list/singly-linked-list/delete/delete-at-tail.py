class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        current = self.head

        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def delete_at_tail(self):
        if self.head is None or self.head.next is None:
            return None  # # list is empty or has only one node

        current = self.head
        while current.next.next is not None:   # stop at the SECOND-to-last node
            current = current.next

        current.next = None
        return self.head

l1 = LinkedList()
l1.head = Node("A")
l1.head.next = Node("B")
l1.head.next.next = Node("C")
print("Before Delete the element at the end: ")
l1.traverse()

l1.delete_at_tail()

print("After Delete the element at the end: ")
l1.traverse()
