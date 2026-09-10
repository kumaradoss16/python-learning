class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

def hash_key(key, num_buckets):
    return hash(key) % num_buckets


def insert_or_update(buckets, key, value):
    index = hash_key(key, len(buckets))
    current = buckets[index]
    while current is not None:
        if current.key == key:
            current.value = value  # key found - overwrite
            return
        current = current.next

    # key is not found
    new_node = Node(key, value)
    new_node.next = buckets[index]
    buckets[index] = new_node


buckets = [None] * 5
insert_or_update(buckets,"Alice", 100)
insert_or_update(buckets,"Bob", 200)
insert_or_update(buckets,"Alice", 300)
insert_or_update(buckets,"Kennedy", 400)


for idx, bucket in enumerate(buckets):
    print(f"Buckest {idx}")

    current = bucket
    while current is not None:
        print(f"    {current.key} -> {current.value}")
        current = current.next
