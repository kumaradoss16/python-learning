queue = []
def enqueue():
    element = input("Enter the element: ")
    queue.append(element)
    print(element, "is added to queue")

def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        element = queue.pop(0)
        print(element, "is removed from queue")

def display():
    print(queue)

while True:
    choice = int(input("Select the operation 1.add 2.remove 3.show 4.quit: "))
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Invalid choice")