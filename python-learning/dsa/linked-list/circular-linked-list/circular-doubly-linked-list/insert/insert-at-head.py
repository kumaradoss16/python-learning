# A Single node in the circular doubly linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


def insert_at_head_by_value(head, value):
    new_node = Node(value)

    if head is None:
        new_node.prev = new_node
        new_node.next = new_node
        return new_node

    tail = head.prev

    new_node.next = head
    new_node.prev = tail
    tail.next = new_node
    head.prev = new_node

    return new_node

head = Node("A")
node_b = Node("B")
node_c = Node("C")

head.next = node_b
node_b.next = node_c
node_c.next = head

head.prev = node_c
node_b.prev = head
node_c.prev = node_b

head = insert_at_head_by_value(head, "X")

current = head
for _ in range(4):
    print(current.value, end=" -> ")
    current = current.next

print(current.value)

