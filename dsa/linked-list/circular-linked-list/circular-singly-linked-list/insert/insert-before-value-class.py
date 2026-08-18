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

    def insert_before_value(self, target_value, new_value):
        if self.head is None:
            return False

        if self.head.value == target_value:
            self.insert_at_head(new_value)
            return True

        current = self.head
        while current.next is not self.head:
            if current.next.value == target_value:
                new_node = Node(new_value)
                new_node.next = current.next
                current.next = new_node

                return True
            current = current.next
        return False


csll = CircularSinglyLinkedList()
csll.head = Node("A")
csll.node_b = Node("B")
csll.tail = Node("C")

csll.head.next = csll.node_b
csll.node_b.next = csll.tail
csll.tail.next = csll.head

csll.insert_before_value("B", "X")
csll.traverse()



