class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0


    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            new_node.next = new_node
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node

        self._size += 1


    def delete(self, value):
        if self.head is None:
            return False

        current = self.head
        previous = self.tail
        while True:
            if current.value == value:
                if current is self.head and current is self.tail:
                    self.head = None
                    self.tail = None
                elif current is self.head:
                    self.head = current.next
                    self.tail.next = self.tail
                elif current is self.tail:
                    previous.next = self.head
                    self.tail = previous
                else:
                    previous.next = current.next

                self._size -= 1
                return True

            previous = current
            current = current.next
            if current is self.head:
                break

        return False

    def to_list(self):
        if self.head is None:
            return []

        result = []
        current = self.head
        while True:
            result.append(current.value)
            current = current.next
            if current is self.head:
                break
        return result

    def size(self):
        return self._size

csll = CircularSinglyLinkedList()
csll.append(1)
csll.append(2)
csll.append(3)
csll.prepend(0)
print(csll.to_list())      # [0, 1, 2, 3]
csll.delete(2)
print(csll.to_list())      # [0, 1, 3]
