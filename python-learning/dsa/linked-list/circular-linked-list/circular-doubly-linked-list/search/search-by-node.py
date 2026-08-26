class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def search_by_node(head, target_node):
    if head is None:
        return False

    current = head
    while True:
        if current is target_node:
            return True
        current = current.next
        if current is head:
            return False


# Create circular doubly linked list
head = Node("A")
node_b = Node("B")
tail = Node("C")

head.next = node_b
node_b.next = tail
tail.next = head

head.prev = tail
node_b.prev = head
tail.prev = node_b


if search_by_node(head, node_b):
    print("Found")
else:
    print("Not found")
