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


def insert_before_value(head, tail, target_value, new_value):
    # Case 1: check if list is empty
    if head is None:
        return head, tail

    # Case 2: target value is at the head
    if head.value == target_value:
        return insert_at_head_by_value(head, tail, new_value)

    # Search for the node before the target
    current = head
    while current.next is not head:

        if current.next.value == target_value:
            new_node = Node(new_value)
            new_node.next = current.next
            current.next = new_node

            return head, tail
        current = current.next
    return head, tail

head = Node("A")
node_b = Node("B")
tail = Node("C")

head.next = node_b
node_b.next = tail
tail.next = head

insert_before_value(head, tail, "B", "X")
traverse(head)




