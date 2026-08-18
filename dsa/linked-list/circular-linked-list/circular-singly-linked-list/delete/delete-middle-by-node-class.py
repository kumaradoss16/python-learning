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

    def delete_middle(self, target_node):
        if self.head is None:
            return
        if target_node is self.head:
            self.delete_at_head()
            return
        if target_node is self.tail:
            self.delete_at_end()
            return

        previous = self.head
        while previous.next is not target_node:
            previous = previous.next
        previous.next = target_node.next




csll = CircularSinglyLinkedList()
csll.head = Node("A")
csll.node_b = Node("B")
csll.node_c = Node("C")
csll.tail = Node("D")

csll.head.next = csll.node_b
csll.node_b.next = csll.node_c
csll.node_c.next = csll.tail
csll.tail.next = csll.head

csll.delete_middle(csll.node_c)
csll.traverse()