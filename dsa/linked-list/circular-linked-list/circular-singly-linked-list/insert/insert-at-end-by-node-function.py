class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def insert_at_end_by_node(head, tail, new_node):
    if head is None:
        new_node.next = new_node
        return new_node, new_node

    new_node.next= head
    tail.next = new_node
    return head, new_node

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

new_node = Node("X")
head, tail = insert_at_end_by_node(head, tail, new_node)
traverse(head)



