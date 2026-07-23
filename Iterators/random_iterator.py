import random

class RandomNumbers:
    def __init__(self, start, end , limit) -> None:
        self.start = start
        self.end = end
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.limit:
            self.count += 1
            return random.randint(self.start, self.end)

        raise StopIteration


numbers = RandomNumbers(1, 100, 10)
for number in numbers:
    print(number)



"""
Output:
8
24
96
81
18
97
99
74
42
71
"""
