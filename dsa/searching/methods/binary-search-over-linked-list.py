def binary_search_iterative(arr, target):
    low, high = 0, len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def binary_search_over_linked_list(head, target):
    values = []
    current = head
    while current is not None:
        values.append(current.value)
        current = current.next

    values.sort()

    return binary_search_iterative(values, target)


head = Node(9)
head.next = Node(3)
head.next.next = Node(7)
head.next.next.next = Node(1)

print(binary_search_over_linked_list(head, 1))

