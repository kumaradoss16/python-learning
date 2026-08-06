class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        current = self.head

        while current is not None:
            print(current.value, end=" -> ")
            current = current.next

        print("None")

    def insert_at_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

l1 = LinkedList()
l1.head = Node("A")
l1.head.next = Node('B')
l1.head.next.next = Node("C")

l1.insert_at_head("X")
l1.traverse()