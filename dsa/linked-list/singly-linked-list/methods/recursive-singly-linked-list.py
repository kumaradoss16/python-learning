class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Count the number of node recursively
def recursive_length(node):
    if node is None:
        return 0
    return 1 + recursive_length(node.next)

# Search for a value recursively
def recursive_search(node, target):
    if node is None:
        return False

    if node.value == target:
        return True

    return recursive_search(node.next, target)

# Print the linked list recursively
def recursive_print(node):
    if node is None:
        return

    print(node.value, end=" ")
    recursive_print(node.next)


head = Node("A")
head.next = Node("B")
head.next.next = Node("C")

print(recursive_length(head))
print(recursive_search(head, "B"))
recursive_print(head)
