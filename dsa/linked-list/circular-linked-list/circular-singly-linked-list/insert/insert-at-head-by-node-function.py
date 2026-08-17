class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def insert_at_head_by_node(head, tail, new_node):
    if head is None:
        new_node.next = new_node
        return new_node, new_node

    new_node.next = head
    tail.next = new_node
    return new_node, tail

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

head = Node("B")
tail = Node("C")
head.next = tail
tail.next = head

new_node = Node("A")

head, tail = insert_at_head_by_node(head, tail, new_node)

traverse(head)

