class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        current = self.head

        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

l1 = LinkedList()
l1.head = Node("A")
l1.head.next = Node('B')
l1.head.next.next = Node("C")

print("Before Reverse:")
l1.traverse()

print("After Reverse:")
l1.reverse()
l1.traverse()