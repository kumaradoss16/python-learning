class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

def hash_key(key, num_buckets):
    return hash(key) % num_buckets


def get(buckets, key):
    index = hash_key(key, len(buckets))
    current = buckets[index]

    while current is not None:
        if current.key == key:
            return current.value
        current = current.next

    return None


def contains_key(buckets, key):
    return get(buckets, key) is not None


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

print("Alice exists:", contains_key(buckets, "Alice"))
print("David exists:", contains_key(buckets, "David"))
