class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def traverse(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current .next
        print("None")

    def insert_before_node(self, target_value, new_value):
        if target_value is None:
            return False
        """
        new_node
         ├── value = X
         ├── next  = None
         └── prev  = None
        """
        new_node = Node(new_value)
        new_node.next = target_value   # X.next = B
        new_node.prev = target_value.prev   # X.prev = A

        if target_value.prev is not None:
            target_value.prev.next = new_node   # A.next = X
        else:
            self.head = new_node

        target_value.prev = new_node    # B.prev = X

        return True


dll = DoublyLinkedList()
dll.head = Node("A")
dll.head.next = Node("B")
dll.head.next.prev = dll.head
dll.head.next.next = Node("C")
dll.head.next.next.prev = dll.head.next
dll.tail = dll.head.next.next

dll.insert_before_node(dll.head.next, "X")
dll.traverse()




