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


    def update_by_value(self, old_value, new_value):
        if self.head is None:
            return False

        current = self.head
        while True:
            if current.value == old_value:
                current.value = new_value
                return True
            current = current.next
            if current is self.head:
                return False

csll = CircularSinglyLinkedList()
csll.head = Node("A")
csll.node_b = Node("B")
csll.node_c = Node("C")
csll.tail = Node("D")

csll.head.next = csll.node_b
csll.node_b.next = csll.node_c
csll.node_c.next = csll.tail
csll.tail.next = csll.head

csll.update_by_value("C", "X")
csll.traverse()
