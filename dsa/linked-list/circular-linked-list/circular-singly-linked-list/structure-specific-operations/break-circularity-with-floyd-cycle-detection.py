class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def break_circularity(head):
    if head is None or head.next is None:
        return
    # Detect cycle
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            break
    else:
        return
    # Find cycle start
    slow = head

    while slow is not fast:
        slow = slow.next
        fast = fast.next

    cycle_start = slow

    # Find last node in cycle
    current = cycle_start
    while current.next is not cycle_start:
        current = current.next

    # Break cycle
    current.next = None


def traverse(head):
    if head is None:
        print("List is empty")
        return

    current = head
    visited = set()

    while current is not None:
        if current in visited:
            print(f"(cycle back to {current.value})")
            break

        print(current.value, end=" -> ")
        visited.add(current)
        current = current.next


node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")

# Connect nodes
node_a.next = node_b
node_b.next = node_c
node_c.next = node_d

# Create cycle
node_d.next = node_b

traverse(node_a)
break_circularity(node_a)

current = node_a
while current is not None:
    print(current.value, end=" -> ")
    current = current.next
print("None")