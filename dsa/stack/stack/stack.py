stack = []

def push_element():
    if len(stack) == num:
        print("Stack is full")
    else:
        element = input("Enter the element: ")
        stack.append(element)
        print(stack)

def pop_element():
    if not stack:
        print("Stack is empty")
    else:
        element = stack.pop()
        print("Element is removed")
        print(element)

num = int(input("Enter the limit of stack: "))   # Used to prevent the print load
while True:
    choice = int(input("Enter your Operation (1. Push  2. Pop  3. Exit): "))
    if choice == 1:
        push_element()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("Invalid choice")