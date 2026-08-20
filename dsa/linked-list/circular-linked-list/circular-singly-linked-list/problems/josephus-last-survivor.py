class PersonNode:
    def __init__(self, name):
        self.name = name
        self.next = None

def josephus_last_survivor(names, k):
    if not names:
        return None

    # Build the circular list
    head = PersonNode(names[0])
    current = head
    for name in names[1:]:
        current.next = PersonNode(name)
        current = current.next
    current.next = head  # Close the circle

    current = head
    previous = None
    remaining = len(names)

    while remaining > 1:
        for _ in range(k - 1):
            previous = current
            current = current.next

        print(f"{current.name} is eliminated")
        previous.next = current.next
        current = previous.next
        remaining -= 1

    return current.name

survivor  = josephus_last_survivor(["Alice", "Bob", "Carol", "Dave", "Eve"], k = 2)
print(f"Survivor : {survivor}")