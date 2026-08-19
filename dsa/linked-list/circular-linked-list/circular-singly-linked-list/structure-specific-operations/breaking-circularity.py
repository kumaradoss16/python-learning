class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def break_circularity(head):
    if head is None:
        return
    current = head
    while current.next is not head:
        current = current.next
    current.next = None

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


node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")

# Connect nodes
node_a.next = node_b
node_b.next = node_c
node_c.next = node_d

# Create cycle
node_d.next = node_a

traverse(node_a)
break_circularity(node_a)

current = node_a
while current is not None:
    print(current.value, end=" -> ")
    current = current.next
print("None")