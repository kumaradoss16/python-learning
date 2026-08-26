class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


def insert_before_value(head, target_value, new_value):
    if head is None:
        return None

    current = head
    while True:
        if current.value == target_value:
            new_node = Node(new_value)
            prev_node = current.prev

            new_node.next = current
            new_node.prev = prev_node
            current.prev = new_node
            prev_node.next = new_node

            if current is head:
                return new_node
            return head

        current = current.next
        if current is head:
            break

    return head


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

head = insert_before_value(head, "B", "X")

# Traverse
current = head

for _ in range(4):
    print(current.value, end=" -> ")
    current = current.next

print(current.value)