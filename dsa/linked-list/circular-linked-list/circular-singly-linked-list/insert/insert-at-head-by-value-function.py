class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def insert_at_head_by_value(head, tail, value):
    new_node  = Node(value)
    # If there is no existing node, both head and tail are the same node
    if head is None:
        new_node.next = new_node
        return new_node, new_node
    # If the list is not empty
    new_node.next = head   # New node point to the old head
    tail.next = new_node   # old tail point to the new head
    return new_node, tail

head = Node("B")
tail = Node("C")
head.next = tail
tail.next = head

head, tail = insert_at_head_by_value(head, tail, "A")
head, tail = insert_at_head_by_value(head, tail, "X")
print(head.value, tail.value)