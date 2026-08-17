class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def insert_after_value(head, target_value, value):
    if head is None:
        return
    current = head
    while True:
        if current.value == target_value:
            new_node = Node(value)
            new_node.next = current.next
            current.next = new_node
            return
        current = current.next
        if current is head:
            return

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

insert_after_value(head,"B", "X")
traverse(head)