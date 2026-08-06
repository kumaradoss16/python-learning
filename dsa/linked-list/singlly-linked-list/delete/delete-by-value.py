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

    def delete_by_value(self, target):
        current = self.head
        while current.next is not None:
            if current.next.value == target:
                current.next = current.next.next
                return self.head
            current = current.next

        return self.head

l1 = LinkedList()
l1.head = Node("A")
l1.head.next = Node("B")
l1.head.next.next = Node("C")

l1.delete_by_value("B")
l1.traverse()