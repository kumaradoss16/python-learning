class HybridLookup:
    def __init__(self, sorted_data):
        self.sorted_data = sorted_data
        self.exact_lookup = {value: index for index, value in enumerate(sorted_data)}

    def find_exact(self, target):
        return self.exact_lookup.get(target, -1)

    def find_closest(self, target):
        low, high = 0, len(self.sorted_data) - 1
        while low < high:
            mid = (low + high) // 2
            if self.sorted_data[mid] < target:
                low = mid + 1
            else:
                high = mid

        return self.sorted_data[low]

hybrid = HybridLookup([2, 5, 8, 12, 16, 23, 38])
print(hybrid.find_exact(12))
print(hybrid.find_closest(16))