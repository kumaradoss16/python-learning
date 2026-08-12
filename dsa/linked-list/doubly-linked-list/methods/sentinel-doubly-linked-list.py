class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class SentinelDoublyLinkedList:
    def __init__(self):
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    def append(self, value):
        new_node = Node(value)
        last_real_node = self.sentinel.prev   # last_real_node = self.sentinel

        new_node.prev = last_real_node   # A.prev = self.sentinel
        new_node.next = self.sentinel   # A.next = self.sentinel       sentinel <-> A <-> sentinel
        last_real_node.next = new_node   # self.sentinel.next = A
        self.sentinel.prev = new_node   # self.sentinel.prev = A

    def to_list(self):
        result = []
        current = self.sentinel.next
        while current is not self.sentinel:
            result.append(current.value)
            current = current.next
        return result


sdll = SentinelDoublyLinkedList()
sdll.append("A")
sdll.append("B")
sdll.append("C")

print(sdll.to_list())