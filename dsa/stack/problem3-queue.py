from queue import LifoQueue

stack = LifoQueue(3)  # Initialize a thread-safe queue with limit

# Put elements into the queue
stack.put(10)
stack.put(20)
stack.put(30)

# Get elements out of the queue
print(stack.get())
print(stack.get())