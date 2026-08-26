class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


def insert_before_node(target_node, new_node, head):
    prev_node = target_node.prev

    new_node.next = target_node
    new_node.prev = prev_node
    prev_node.next = new_node
    target_node.prev = new_node


    if target_node is head:
        return new_node
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

new_node = Node("X")
head = insert_before_node(node_b, new_node, head)

# Traverse
current = head

for _ in range(4):
    print(current.value, end=" -> ")
    current = current.next

print(current.value)