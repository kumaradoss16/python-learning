class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def traverse(head):
    if head is None:
        print("List is empty")
        return

    current = head
    while True:
        print(current.value, end=" -> ")
        current = current.next

        if current == head:
            break
    print("(back to head)")

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


def insert_before_node(head, target_node, value):
    if head is target_node:
        new_head, tail = insert_at_head_by_value(head, find_tail(head), value)
        return new_head

    current = head
    while current.next is not target_node:
        current = current.next

    new_node = Node(value)
    new_node.next = target_node
    current.next = new_node
    return head

def find_tail(head):
    current = head
    while current.next is not head:
        current = current.next
    return current



head = Node("A")
node_b = Node("B")
tail = Node("C")

head.next = node_b
node_b.next = tail
tail.next = head

insert_before_node(head, node_b, "X")
traverse(head)


