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


head = Node("A")
node_b = Node("B")
tail = Node("C")

head.next = node_b
node_b.next = tail
tail.next = head

head, tail = delete_at_end(head, tail)
traverse(head)