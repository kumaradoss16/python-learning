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


"""
Output:

Enter the limit of stack: 4
Enter your Operation (1. Push  2. Pop  3. Exit): 1
Enter the element: 10
['10']
Enter your Operation (1. Push  2. Pop  3. Exit): 1
Enter the element: 20
['10', '20']
Enter your Operation (1. Push  2. Pop  3. Exit): 1
Enter the element: 30
['10', '20', '30']
Enter your Operation (1. Push  2. Pop  3. Exit): 1
Enter the element: 40
['10', '20', '30', '40']
Enter your Operation (1. Push  2. Pop  3. Exit): 1
Stack is full
Enter your Operation (1. Push  2. Pop  3. Exit): 2
Element is removed
40
Enter your Operation (1. Push  2. Pop  3. Exit): 2
Element is removed
30
Enter your Operation (1. Push  2. Pop  3. Exit): 2
Element is removed
20
Enter your Operation (1. Push  2. Pop  3. Exit): 2
Element is removed
10
Enter your Operation (1. Push  2. Pop  3. Exit): 2
Stack is empty
Enter your Operation (1. Push  2. Pop  3. Exit): 3
"""
