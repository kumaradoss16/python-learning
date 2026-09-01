class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def reverse_segment(start_node, length, forward=True):
    stack = []
    current = start_node
    for _ in range(length):
        stack.append(current.value)
        current = current.next if forward else current.prev

    current = start_node
    while stack:
        current.value = stack.pop()
        current = current.next if forward else current.prev

node_a, node_b, node_c, node_d = Node("A"),Node("B") ,Node("C") ,Node("D")
node_a.next, node_b.next,node_c.next ,node_d.next = node_b, node_c, node_d, node_a
node_a.prev,node_b.prev ,node_c.prev ,node_d.prev = node_d, node_a, node_b, node_c

print("Original:")
current, result = node_a, []
for _ in range(4):
    result.append(current.value)
    current = current.next
print(result)

reverse_segment(node_a, 3, forward=True)
print("After Reverse:")
current, result = node_a, []
for _ in range(4):
    result.append(current.value)
    current = current.next
print(result)