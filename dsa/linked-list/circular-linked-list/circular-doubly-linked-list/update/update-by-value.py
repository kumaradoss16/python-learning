class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def update_by_value(head, old_value, new_value):
    if head is None:
        return None

    current = head
    while True:
        if current.value == old_value:
            current.value = new_value
            return head
        current = current.next
        if current is head:
            return head


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


head = update_by_value(head, "B", "X")
# Traverse
current = head

for _ in range(get_length(head)):
    print(current.value, end=" -> ")
    current = current.next

print(current.value)

