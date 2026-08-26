class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def insert_after_node(target_node, new_node):
    next_node = target_node.next

    new_node.prev = target_node
    new_node.next = next_node
    target_node.next = new_node
    next_node.prev = new_node


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

new_node = Node("X")

insert_after_node(node_b, new_node)


# Traverse
current = head

for _ in range(4):
    print(current.value, end=" -> ")
    current = current.next

print(current.value)