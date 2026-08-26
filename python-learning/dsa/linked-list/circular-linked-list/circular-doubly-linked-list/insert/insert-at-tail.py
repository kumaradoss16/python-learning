class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


def insert_at_tail(head, value):
    new_node = Node(value)

    if head is None:
        new_node.next = new_node
        new_node.prev = new_node
        return new_node

    tail = head.prev

    new_node.prev = tail
    new_node.next = head
    tail.next = new_node
    head.prev = new_node

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
head = insert_at_tail(head, "X")


# Traverse
current = head

for _ in range(4):
    print(current.value, end=" -> ")
    current = current.next

print(current.value)