class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self, target) -> bool:
        current = self.head
        while current is not None:
            if current.value == target:
                return True
            current = current.next
        return False


l1 = LinkedList()
l1.head = Node("A")
l1.head.next = Node('B')
l1.head.next.next = Node("C")

print(l1.traverse("C"))
print(l1.traverse("Z"))
