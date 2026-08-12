class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        # Sentinel nodes
        self.head = Node(None, None)
        self.tail = Node(None, None)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = Node

    # Lookup operation of the LRU Cache
    def get(self, key):
        if key not in self.cache:
            return None

        node = self.cache[key]

        self.remove(node)
        self.add_to_front(node)

        return node.value

    # Insert / Update operations
    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]

            node.value = value

            self.remove(node)
            self.add_to_front(node)
            return
        node = Node(key, value)

        self.cache[key] = node
        self.add_to_front(node)
        if len(self.cache) > self.capacity:
            lru = self.tail.prev

            self.remove(lru)
            del self.cache[lru.key]


cache = LRUCache(3)

cache.put("A", 100)
cache.put("B", 200)
cache.put("C", 300)

print(cache.get("A"))
print(cache.cache)

cache.put("D", 400)
print(cache.cache)
