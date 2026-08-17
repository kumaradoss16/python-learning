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

    def insert_after_value(self, target_value, new_value):
        if self.head is None:
            return
        current = self.head
        while True:
            if current.value == target_value:
                new_node = Node(new_value)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            if current is self.head:
                return

csll = CircularSinglyLinkedList()

csll.head = Node("A")
node_b = Node("B")
csll.tail = Node("C")

csll.head.next = node_b
node_b.next = csll.tail
csll.tail.next = csll.head

csll.insert_after_value("B", "X")
csll.traverse()