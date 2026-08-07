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


    def insert_after_node(self, target, new_value):
        if  target is None:
            return False
        new_node = Node(new_value)
        new_node.next = target.next
        target.next = new_node
        return True


l1 = LinkedList()
l1.head = Node("A")
l1.head.next = Node('B')
l1.head.next.next = Node("C")

l1.insert_after_node(l1.head.next, "X")
l1.traverse()