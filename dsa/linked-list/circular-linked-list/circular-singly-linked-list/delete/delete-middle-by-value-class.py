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

    def delete_at_end(self):
        if self.head is None:
            return

        if self.head is self.tail:
            self.head = self.tail = None
            return

        current = self.head
        while current.next is not self.tail:
            current = current.next
        current.next = self.head
        self.tail = current

    def delete_middle(self, target_value):
        if self.head is None:
            return
        if self.head.value == target_value:
            self.delete_at_head()
            return
        if self.tail.value == target_value:
            self.delete_at_end()
            return

        previous = self.head
        current = self.head.next
        while current is not self.head:
            if current.value == target_value:
                previous.next = current.next
                return
            previous = current
            current = current.next


csll = CircularSinglyLinkedList()
csll.head = Node("A")
csll.node_b = Node("B")
csll.node_c = Node("C")
csll.tail = Node("D")

csll.head.next = csll.node_b
csll.node_b.next = csll.node_c
csll.node_c.next = csll.tail
csll.tail.next = csll.head

csll.delete_middle("B")
csll.traverse()