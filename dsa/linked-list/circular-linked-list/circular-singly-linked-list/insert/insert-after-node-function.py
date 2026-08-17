class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def insert_after_node(target_node, value):
    new_node = Node(value)
    new_node.next = target_node.next
    target_node.next = new_node


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

insert_after_node(node_b, "X")
traverse(head)