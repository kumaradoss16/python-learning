class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_before_node(self, target, new_value):
        new_node = Node(new_value)

        # List is empty
        if self.head is None:
            return False

        # target is the head itself
        if self.head.value == target:
            new_node.next = self.head
            self.head = new_node
            return True

        # traverse the list, always looking one node ahead

        current = self.head
        while current.next is not None:
            if current.next.value == target:
                new_node.next = current.next
                current.next = new_node
                return True
            current = current.next

        return False  # target not found

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

l1 = LinkedList()
l1.head = Node("A")
l1.head.next = Node('B')
l1.head.next.next = Node("C")

l1.insert_before_node("C", "X")
l1.traverse()

