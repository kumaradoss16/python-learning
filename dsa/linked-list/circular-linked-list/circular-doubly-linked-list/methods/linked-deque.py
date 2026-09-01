class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedDeque:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, value):
        new_node = Node(value)
        if self.head is None:
            new_node.next = new_node.prev = self.head
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node

    def push_back(self, value):
        new_node = Node(value)
        if self.head is None:
            new_node.next = new_node.prev = new_node
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node


    def pop_front(self):
        if self.head is None:
            raise  IndexError("pop from empty deque")
        value = self.head.value
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
        return value

    def pop_back(self):
        if self.head is None:
            raise  IndexError("pop from empty deque")
        value = self.tail.value
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
        return value

dq = LinkedDeque()
dq.push_back(1)
dq.push_back(2)
dq.push_front(0)
print(dq.pop_front())
print(dq.pop_back())

