class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def is_circular(head):
    if head is None:
        return False
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

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

print(is_circular(node_a))