class Count:
    def __init__(self, end):
        self.current = 1
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= self.end:
            value = self.current
            self.current += 1
            return value
        
        raise StopIteration
    

counter = Count(5)

for num in counter:
    print(num)


"""
Output:
1
2
3
4
5
""
