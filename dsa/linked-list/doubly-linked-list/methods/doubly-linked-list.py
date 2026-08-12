class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1


    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self._size += 1


    def delete(self, value):
        current = self.head
        while current:
            if current.value == value:
                # Check the value is not at the head node
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                # Check the value is not at the tail node
                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                self._size -= 1
                return True
            current = current.next

        return False

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next

        return result

    def to_list_reversed(self):
        result = []
        current = self.tail
        while current:
            result.append(current.value)
            current = current.prev

        return result

    def size(self):
        return self._size


dll = DoublyLinkedList()

dll.append("A")
dll.append("B")
dll.append("C")
dll.prepend("Start")
print(dll.to_list())            # ['Start', 'A', 'B', 'C']
print(dll.to_list_reversed())   # ['C', 'B', 'A', 'Start']
dll.delete("B")
print(dll.to_list())


