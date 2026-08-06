from collections import deque
import time

class RateLimiter:
    def __init__(self, max_requests, window_seconds):
        self.max_request = max_requests
        self.window_seconds = window_seconds
        self.timestamp = deque()

    def allow_request(self):
        now = time.time()

        while self.timestamp and now - self.timestamp[0] > self.window_seconds:
            self.timestamp.popleft()

        if len(self.timestamp) < self.max_request:
            self.timestamp.append(now)
            return True

        return False

limiter = RateLimiter(max_requests=3, window_seconds=10)
print(limiter.allow_request())   # True
print(limiter.allow_request())   # True
print(limiter.allow_request())   # True
print(limiter.allow_request())   # False — limit hit within the window
