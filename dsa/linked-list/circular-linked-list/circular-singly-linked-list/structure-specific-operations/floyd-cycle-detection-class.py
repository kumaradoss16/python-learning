class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_circular(self):
        if self.head is None:
            return False
        slow = fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

csll = CircularSinglyLinkedList()
csll.node_a = Node("A")
csll.node_b = Node("B")
csll.node_c = Node("C")
csll.node_d = Node("D")

# Connect nodes
csll.node_a.next = csll.node_b
csll.node_b.next = csll.node_c
csll.node_c.next = csll.node_d

# Create cycle
csll.node_d.next = csll.node_b

print(csll.is_circular())