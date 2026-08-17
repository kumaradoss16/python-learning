from collections import deque

class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.window = deque()
        self.window_sum = 0

    def next(self, value):
        self.window.append(value)
        self.window_sum += value

        if len(self.window) > self.size:
            oldest = self.window.popleft()
            self.window_sum -= oldest

        return self.window_sum / len(self.window)


ma = MovingAverage(3)
print(ma.next(1))
print(ma.next(10))
print(ma.next(3))
print(ma.next(5))
print(ma.next(6))
print(ma.next(7))
