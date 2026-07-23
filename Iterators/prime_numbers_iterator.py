class PrimeNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):
        while self.current < self.limit:
            number = self.current
            self.current += 1

            is_prime = True
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False
                    break

            if is_prime:
                return number

        raise StopIteration

num = int(input("Enter the number = "))
prime = PrimeNumbers(num)
print(f"Prime Numbers between {2} to {num}:")

for number in prime:
    print(number)
