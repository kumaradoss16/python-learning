class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def delete_by_value(head, target_value):
    if head is None:
        return None

    current = head
    while True:
        if current.value == target_value:
            if current.next is current:
                return None

            prev_node = current.prev
            next_node = current.next
            prev_node.next = next_node
            next_node.prev = prev_node

            if current is head:
                return next_node
            return head

        current = current.next
        if current is head:
            break

    return head  # value not found

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

head = delete_by_value(head, "B")

# Traverse
current = head

for _ in range(get_length(head)):
    print(current.value, end=" -> ")
    current = current.next

print(current.value)