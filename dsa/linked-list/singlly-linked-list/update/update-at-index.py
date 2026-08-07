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

    def update_at_index(self, index, new_value):
        current = self.head
        current_index = 0

        while current is not None:
            if current_index == index:
                current.value = new_value
                return True
            current = current.next
            current_index += 1

        return False


l1 = LinkedList()
l1.head = Node("A")
l1.head.next = Node("B")
l1.head.next.next = Node("C")
l1.head.next.next.next = Node("D")

print("Traversal of LinkedList Before Update: ")
l1.traverse()


l1.update_at_index(2, "X")
print("Traversal of LinkedList After Update: ")
l1.traverse()
