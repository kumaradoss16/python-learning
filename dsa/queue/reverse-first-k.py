from collections import deque

def reverse_first_k(queue, k):
    if k <= 0 or k > len(queue):
        return queue

    stack = []

    for _ in range(k):
        stack.append(queue.popleft())

    while stack:
        queue.append(stack.pop())

    for _ in range(len(queue) - k):
        queue.append(queue.popleft())

    return queue


q = deque([1, 2, 3, 4, 5])
print(list(reverse_first_k(q, 2)))