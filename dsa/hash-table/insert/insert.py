class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

def hash_key(key, num_buckets):
    return hash(key) % num_buckets


def insert(buckets, key, value):
    index = hash_key(key, len(buckets))
    new_node = Node(key, value)
    new_node.next = buckets[index]  # Point the new_node next into a buckets
    buckets[index] = new_node

# Create 5 empty buckets
buckets = [None] * 5

# Insert some key-value pairs
insert(buckets, "Alice", 100)
insert(buckets, "Bob", 200)
insert(buckets, "John", 300)
insert(buckets, "Kevin", 400)
insert(buckets, "Kennedy", 500)

# Display the has table
for idx, bucket in enumerate(buckets):
    print(f"Bucket {idx}")

    current = bucket

    while current is not None:
        print(f"    {current.key} -> {current.value}")
        current = current.next

