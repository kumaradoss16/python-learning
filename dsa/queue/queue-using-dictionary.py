class DictQueue:
    def __init__(self):
        self.storage = {}
        self.front = 0  # points to the NEXT item to be removed
        self.rear = 0   # points to the NEXT item to be removed

    def enqueue(self, value):
        self.storage[self.rear] = value
        self.rear += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, nothing to dequeue")
            return None

        value = self.storage[self.front]
        del self.storage[self.front]

        self.front += 1

        return value

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.storage[self.front]

    def is_empty(self):
        return self.front == self.rear

    def size(self):
        return self.rear - self.front

q = DictQueue()

q.enqueue("A")   # storage: {0: "A"}
q.enqueue("B")   # storage: {0: "A", 1: "B"}
q.enqueue("C")   # storage: {0: "A", 1: "B", 2: "C"}

print(q.dequeue())   # A  -> slot 0 removed, front moves to 1
print(q.peek())      # B  -> next in line
print(q.dequeue())   # B  -> slot 1 removed, front moves to 2
print(q.size())      # 1  -> only C left, in slot 2