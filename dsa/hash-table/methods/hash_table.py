class HashTable:
    class _Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self, initial_bucket=8):
        self.buckets = [None] * initial_bucket
        self.size = 0


    def _hash(self, key):
        return hash(key) % len(self.buckets)

    def put(self, key, value):
        index = self._hash(key)
        current = self.buckets[index]

        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next

        new_node = self._Node(key, value)
        new_node.next = self.buckets[index]
        self.buckets[index] = new_node
        self.size += 1

        if self.size / len(self.buckets) > 0.75:
            self._resize()


    def get(self, key):
        index = self._hash(key)
        current = self.buckets[index]

        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def contains(self, key):
        return self.get(key) is not None


    def delete(self, key):
        index = self._hash(key)
        current = self.buckets[index]
        previous = None

        while current is not None:
            if current.key == key:
                if previous is None:
                    self.buckets[index] = current.next
                else:
                    previous.next = current.next
                self.size -= 1

            previous = current
            current = current.next

        return False

    def _resize(self):
        old_buckets = self.buckets
        self.buckets = [None] * (len(old_buckets) * 2)
        self.size = 0

        for head in old_buckets:
            current = head
            while current is not None:
                self.put(current.key, current.value)
                current = current.next

    def __len__(self):
        return self.size

    def keys(self):
        result = []
        for head in self.buckets:
            current = head
            while current is not None:
                result.append(current.key)
                current = current.next
        return result

ht = HashTable()

ht.put("name", "Kumar")
ht.put("age", 25)
ht.put("city", "Puducherry")
ht.put("course", "Python")
ht.put("role", "IT Trainer")

print("Keys:", ht.keys())
print("Size:", len(ht))

print("Name:", ht.get("name"))
print("Age:", ht.get("age"))

print("Contains 'city':", ht.contains("city"))
print("Contains 'salary':", ht.contains("salary"))

ht.put("age", 26)
print("Updated age:", ht.get("age"))

ht.delete("city")
print("After deleting city:", ht.keys())
print("Final size:", len(ht))




