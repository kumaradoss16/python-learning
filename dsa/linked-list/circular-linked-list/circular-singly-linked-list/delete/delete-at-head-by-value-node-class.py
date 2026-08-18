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


    def delete_at_head(self):
        if self.head is None:
            return

        if self.head is self.tail:
            self.head = self.tail = None
            return
        self.head = self.head.next
        self.tail.next = self.head


csll = CircularSinglyLinkedList()
csll.head = Node("A")
csll.node_b = Node("B")
csll.tail = Node("C")

csll.head.next = csll.node_b
csll.node_b.next = csll.tail
csll.tail.next = csll.head

csll.delete_at_head()
csll.traverse()