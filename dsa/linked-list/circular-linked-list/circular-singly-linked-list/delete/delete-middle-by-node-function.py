class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def delete_at_end(head, tail):
    if head is None:
        return None, None

    if head is tail:
        return None, None

    current = head
    while current.next is not tail:
         current = current.next
    current.next = head
    return head, current

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

def delete_at_head(head, tail):
    if head is None:
        return None, None

    if head is tail:
        return None, None

    new_head = head.next
    tail.next = new_head
    return new_head, tail


def delete_at_end(head, tail):
    if head is None:
        return None, None

    if head is tail:
        return None, None

    current = head
    while current.next is not tail:
         current = current.next
    current.next = head
    return head, current


def delete_middle(head, tail, target_node):
    if head is None:
        return head, tail
    if target_node is head:
        return delete_at_head(head, tail)
    if target_node is tail:
        return delete_at_end(head, tail)

    previous = head
    while previous.next is not target_node:
        previous = previous.next

    previous.next = target_node.next
    return head, tail



head = Node("A")
node_b = Node("B")
node_c = Node("C")
tail = Node("D")

head.next = node_b
node_b.next = node_c
node_c.next = tail
tail.next = head

head, tail = delete_middle(head, tail, node_c)
traverse(head)
