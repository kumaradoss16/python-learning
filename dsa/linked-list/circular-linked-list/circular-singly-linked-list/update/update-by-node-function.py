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


def update_by_value(target_node, new_value):
    target_node.value = new_value


head = Node("A")
node_b = Node("B")
node_c = Node("C")
tail = Node("D")

head.next = node_b
node_b.next = node_c
node_c.next = tail
tail.next = head

update_by_value(node_c, "X")
traverse(head)