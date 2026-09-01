class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def insert_at_head(self, value):
        new_node = Node(value)
        if self.head is None:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node
        self._size += 1


    def insert_at_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            new_node.next = new_node.prev = new_node
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            new_node.next = self.head
            self.head.prev = new_node
            self.tail = new_node
        self._size += 1


    def insert_after_node(self, target_node, value):
        new_node = Node(value)
        new_node.next = target_node.next
        new_node.prev = target_node
        target_node.next.prev = new_node
        target_node.next = new_node
        if target_node is self.tail:
            self.tail = new_node
        self._size += 1


    def insert_before_node(self, target_node, value):
        new_node = Node(value)
        new_node.prev = target_node.prev
        new_node.next = target_node
        target_node.prev.next = new_node
        target_node.prev = new_node
        if target_node is self.head:
            self.head = new_node
        self._size += 1


    def delete_at_head(self):
        if self.head is None:
            return
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
        self._size -= 1


    def delete_at_tail(self):
        if self.head is None:
            return
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
        self._size -= 1

    def delete_node(self, target_node):
        if target_node is self.head and target_node is self.tail:
            self.head = self.tail = None
        else:
            target_node.prev.next = target_node.next
            target_node.next.prev = target_node.prev
            if target_node is self.head:
                self.head = target_node.next
            if target_node is self.tail:
                self.tail = target_node.prev
        self._size -= 1


    def delete_by_value(self, target_value):
        if self.head is None:
            return False
        current = self.head
        while True:
            if current.value == target_value:
                self.delete_node(current)
                return True
            current = current.next
            if current is self.head:
                return False


    def search(self, target_value):
        if self.head is None:
            return False
        current = self.head
        while True:
            if current.value == target_value:
                return True
            current = current.next
            if current is self.head:
                return False


    def update_by_value(self, old_value, new_vlaue):
        if self.head is None:
            return False
        current = self.head
        while True:
            if current.value == old_value:
                current.value = new_vlaue
                return True
            current = current.next
            if current is self.head:
                return False


    def is_circular(self):
        if self.head is None:
            return False
        slow = fast = self.head
        while fast is not None and fast.next is not None:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                return True
        return False

    def rotate(self, k):
        if self.head is None or self._size == 0:
            return
        current = self.head
        for _ in range(k % self._size):
            current = current.next
        self.head = current
        self.tail = current.prev

    def to_list_forward(self):
        if self.head is None:
            return []
        result, current = [], self.head
        while True:
            result.append(current.value)
            current = current.next
            if current is self.head:
                break
        return result

    def to_list_backward(self):
        if self.tail is None:
            return []
        result, current = [], self.tail
        while True:
            result.append(current.value)
            current = current.prev
            if current is self.tail:
                break
        return result

    def _size(self):
        return self._size



cdll = CircularDoublyLinkedList()
cdll.insert_at_tail(1)
cdll.insert_at_tail(2)
cdll.insert_at_tail(3)
cdll.insert_at_head(0)
print(cdll.to_list_forward())
print(cdll.to_list_backward())
cdll.delete_at_tail()
print(cdll.to_list_forward())




