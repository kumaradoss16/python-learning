class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def search_by_value(head, target_value):
    # If list is empty
    if head is None:
        return None

    current = head
    while True:
        if current.value == target_value:
            return current
        current = current.next
        # Completed the loop, value not found
        if current is head:
            return None


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


if search_by_value(head, "X"):
    print("Found")
else:
    print("Not found")
