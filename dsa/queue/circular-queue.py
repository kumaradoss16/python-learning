class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.count = 0
        
    def enqueue(self, value):
        if self.count == self.capacity:
            raise OverflowError("Queue is full")

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise IndexError("Queue is empty")

        value = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return value

    def is_full(self):
        return self.count == self.capacity

    def is_empty(self):
        return self.count == 0


cq = CircularQueue(3)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
print(cq.dequeue())
cq.enqueue(4)
print(cq.dequeue())