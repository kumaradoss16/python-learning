class Fibonacci:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.limit:
            if self.count == 0:
                self.count += 1
                return self.first
            elif self.count == 1:
                self.count += 1
                return self.second
            else:
                fib = self.first + self.second
                self.first = self.second
                self.second = fib
                self.count += 1
                return fib
            
        raise StopIteration


fibonacci = Fibonacci(6)

for fib in fibonacci:
    print(fib)



"""
Output:
0
1
1
2
3
5
"""
