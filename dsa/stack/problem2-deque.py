from collections import deque

stack = deque()
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
print(stack.pop())
print(stack[-1])
