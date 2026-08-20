class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_segment_using_stack(head, start_node, length):
    stack = []
    current = start_node
    for _ in range(length):
        stack.append(current.value)
        current = current.next

    current = start_node
    while stack:
        current.value = stack.pop()
        current = current.next

    return head

node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")

node_a.next = node_b
node_b.next = node_c
node_c.next = node_d
node_d.next = node_a

reverse_segment_using_stack(node_a, node_a, 3)
current = node_a
result = []

for _ in range(4):
    result.append(current.value)
    current = current.next

print(result)