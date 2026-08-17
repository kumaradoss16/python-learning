class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, value):
        new_node = Node(value)
        if self.head is None:
            new_node.next = new_node
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.tail.next = new_node
        self.head = new_node

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

    def insert_before_node(self, target_node, value):
        if target_node is self.head:
            self.insert_at_head(value)
            return

        current = self.head
        while current.next is not target_node:
            current = current.next

        new_node = Node(value)
        new_node.next = target_node
        current.next = new_node


csll = CircularSinglyLinkedList()
csll.head = Node("A")
node_b = Node("B")
csll.tail = Node("C")

csll.head.next = node_b
node_b.next = csll.tail
csll.tail.next = csll.head

csll.insert_before_node(node_b, "X")
csll.traverse()
