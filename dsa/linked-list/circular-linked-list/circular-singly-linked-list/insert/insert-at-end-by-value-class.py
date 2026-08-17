class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def traverse(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        while True:
            print(current.value, end=" -> ")
            current = current.next

            if current == self.head:
                break
        print("(back to head)")

    def insert_at_end_by_value(self, value):
        new_node = Node(value)
        if self.head is None:
            new_node.next = new_node
            self.head = self.tail = new_node
            return

        new_node.next = self.head
        self.tail.next = new_node
        self.tail = new_node


csll = CircularSinglyLinkedList()

csll.head = Node("A")
csll.head.next = Node("B")
csll.head.next.next = Node("C")
csll.tail = csll.head.next.next
csll.tail.next = csll.head

csll.insert_at_end_by_value("X")
csll.traverse()
