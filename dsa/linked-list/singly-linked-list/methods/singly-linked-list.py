class Node:
    def __init__(self):
        self.head = None
        self._size = 0

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self._size += 1
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        self._size += 1

    def delete(self, value):
        if self.head is None:
            return False

        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            return True

        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next
        return False

    def search(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_list(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result

    def size(self):
        return self._size


sll = Node()
sll.append(1)
sll.append(2)
sll.append(3)
sll.prepend(0)
print(sll.to_list())      # [0, 1, 2, 3]
print(sll.search(2))      # True
sll.delete(2)
print(sll.to_list())      # [0, 1, 3]
