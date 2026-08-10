class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def traverse(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

    def insert_after_node(self, target_node, value):
        if target_node is None:
            return False

        new_node = Node(value)
        new_node.next = target_node.next
        new_node.prev = target_node

        if target_node.next is not None:
            target_node.next.prev = new_node

        target_node.next = new_node

        if self.tail == target_node:
            self.tail.next = new_node

        return True


dll = DoublyLinkedList()
dll.head = Node("A")
dll.head.next = Node("B")
dll.head.next.prev = dll.head
dll.head.next.next = Node("C")
dll.head.next.next.prev = dll.head.next
dll.tail = dll.head.next.next

dll.insert_after_node(dll.head.next.next, "X")
dll.traverse()


