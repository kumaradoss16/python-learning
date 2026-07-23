class CyclicIterator:
    def __init__(self, data) -> None:
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.data:
            raise StopIteration

        value = self.data[self.index]
        self.index += 1

        if self.index == len(self.data):
            self.index = 0

        return value

letters = ['A', 'B', 'C']
cycle = CyclicIterator(letters)

for letter in cycle:
    print(letter)



""" 
Output:
A
B
C
A
B
C
A
B
C
A
B
C
A
B
C
.....
"""
