class Alphabet:
    def __init__(self):
        self.current = ord('A')
        self.end = ord('Z')

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            letter = chr(self.current)
            self.current += 1
            return letter

        raise StopIteration


alphabet = Alphabet()

for letter in alphabet:
    print(letter)


"""
Output:
A
B
C
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
X
Y
Z
"""
