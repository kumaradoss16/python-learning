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


    def insert_after_node(self, target_node, value):
        new_node = Node(value)
        new_node.next = target_node.next
        target_node.next = new_node
        if target_node is self.tail:
            self.tail = new_node


csll = CircularSinglyLinkedList()

csll.head = Node("A")
node_b = Node("B")
csll.tail = Node("C")

csll.head.next = node_b
node_b.next = csll.tail
csll.tail.next = csll.head

csll.insert_after_node(node_b, "X")
csll.traverse()