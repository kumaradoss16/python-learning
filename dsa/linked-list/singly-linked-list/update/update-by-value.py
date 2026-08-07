class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def update_by_value(self, target_value, new_value):
        current = self.head
        while current:
            if current.value == target_value:
                current.value = new_value
                return True
            current = current.next
        return False


l1 = LinkedList()
l1.head = Node("A")
l1.head.next = Node("B")
l1.head.next.next = Node("C")
l1.head.next.next.next = Node("D")

print("Traversal of LinkedList Before Update: ")
l1.traverse()

if l1.update_by_value("B", "X"):
    print("Update Successful")
else:
    print("Value Not Found")

print("After Update:")
l1.traverse()



