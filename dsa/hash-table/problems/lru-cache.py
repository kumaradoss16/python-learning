class DoublyLinkedNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}

        self.head = DoublyLinkedNode(None, None)
        self.tail = DoublyLinkedNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head


    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.map:
            return -1

        node = self.map[key]
        self._remove(node)
        self._add_to_front(node)
        return node.value

    def put(self, key, value):
        if key in self.map:
            self._remove(self.map[key])

        node = DoublyLinkedNode(key, value)
        self._add_to_front(node)
        self.map[key] = node

        if len(self.map) > self.capacity:
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.map[lru_node.key]

cache = LRUCache(3)
cache.put("A", 100)
cache.put("B", 200)
cache.put("C", 300)

print(cache.get("A"))

cache.put("D", 400)

print(cache.get("B"))
print(cache.get("C"))
print(cache.get("D"))
print(cache.get("A"))
