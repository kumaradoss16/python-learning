class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


def insert_after_value(head, target_value, new_value):
    if head is None:
        return None  # nothing to insert after

    current = head
    while True:
        if current.value == target_value:
            new_node = Node(new_value)
            next_node = current.next

            new_node.prev = current
            new_node.next = next_node
            current.next = new_node
            next_node.prev = new_node
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


# Insert X at the tail
head = insert_after_value(head, "B", "X")


# Traverse
current = head

for _ in range(4):
    print(current.value, end=" -> ")
    current = current.next

print(current.value)



