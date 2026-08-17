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

    def insert_at_head_by_node(self, new_node):
        if self.head is None:
            new_node.next = new_node
            self.head = self.tail = new_node
            return

        new_node.next = self.head
        self.tail.next = new_node
        self.head = new_node


csll = CircularSinglyLinkedList()

csll.head = Node("A")
node_b = Node("B")
node_c = Node("C")
csll.tail = Node("D")

csll.head.next = node_b
node_b.next = node_c
node_c.next = csll.tail
csll.tail.next = csll.head


new_node = Node("X")
csll.insert_at_head_by_node(new_node)
csll.traverse()