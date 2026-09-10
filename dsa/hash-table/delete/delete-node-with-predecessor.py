from operator import index


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

def hash_key(key, num_buckets):
    return hash(key) % num_buckets

def delete_node_with_predecessor(buckets, index, target_node, previous_node):
    if previous_node is None:
        buckets[index] = target_node.next
    else:
        previous_node.next = target_node.next


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

# Delete Alice
key = "Alice"
index = hash_key(key, len(buckets))
current = buckets[index]
previous = None
while current is not None:
    if current.key == key:
        delete_node_with_predecessor(
            buckets,
            index,
            current,
            previous
        )
        break

    previous = current
    current = current.next


for idx, bucket in enumerate(buckets):
    print(f"Bucket {idx}")

    current = bucket
    while current is not None:
        print(f"    {current.key} -> {current.value}")
        current = current.next