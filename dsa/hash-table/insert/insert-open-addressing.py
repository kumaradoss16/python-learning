class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

def hash_key(key, num_buckets):
    return hash(key) % num_buckets

# Insert using linear probing
def insert_open_addressing(table, key, value):
    num_buckets = len(table)
    index = hash_key(key, num_buckets)

    for step in range(num_buckets):
        probe_index = (index + step) % num_buckets
        if table[probe_index] is None or table[probe_index][0] == key:
            table[probe_index] = (key, value)
            return True

    return False


table = [None] * 5

print(insert_open_addressing(table, "Alice", 100))
print(insert_open_addressing(table, "Price", 200))
print(insert_open_addressing(table, "Jason", 300))
print(insert_open_addressing(table, "Kennedy", 400))
print(insert_open_addressing(table, "Kratos", 500))
print(insert_open_addressing(table, "Soap", 600))
print("\nHash Table")

for index, item in enumerate(table):
    print(index, "->", item)
