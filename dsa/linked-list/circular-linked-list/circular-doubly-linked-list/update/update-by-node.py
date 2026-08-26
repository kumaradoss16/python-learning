class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def update_by_node(target_node, new_value):
    target_node.value = new_value


def get_length(head):
    if head is None:
        return 0

    count = 1
    current = head.next

    while current is not head:
        count += 1
        current = current.next

    return count


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


update_by_node(node_b, "X")
# Traverse
current = head

for _ in range(get_length(head)):
    print(current.value, end=" -> ")
    current = current.next

print(current.value)


