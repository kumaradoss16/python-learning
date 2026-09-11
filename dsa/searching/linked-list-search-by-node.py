class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def linked_list_search_by_node(head, target_node):
    current = head
    while current is not None:
        if current is target_node:
            return True
        current = current.next

    return False


node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")

head = node_a
node_a.next = node_b
node_b.next = node_c
node_c.next = node_d

print(linked_list_search_by_node(head, node_c))
