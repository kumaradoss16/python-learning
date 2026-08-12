from collections import deque

dq = deque()

dq.append("A")
dq.append("B")
dq.appendleft("X")

print(list(dq))

dq.pop()
dq.popleft()
print(list(dq))
