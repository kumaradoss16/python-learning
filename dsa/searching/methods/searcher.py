class Searcher:
    def __init__(self, date):
        self.data = date

    def linear_search(self, target):
        for index, value in enumerate(self.data):
            if value == target:
                return index
        return -1

    def binary_search(self, target):
        low, high = 0, len(self.data) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.data[mid] == target:
                return mid
            elif self.data[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def find_first_occurrences(self, target):
        low, high, result = 0, len(self.data) - 1, -1
        while low <= high:
            mid = (low + high) // 2
            if self.data[mid] == target:
                result = mid
                high = mid - 1
            elif self.data[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return result


    def find_last_occurrences(self, target):
        low, high, result = 0, len(self.data) - 1, -1
        while low <= high:
            mid = (low + high) // 2
            if self.data[mid] == target:
                result = mid
                low = mid + 1
            elif self.data[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return result


    def count_occurrences(self, target):
        first = self.find_first_occurrences(target)
        if first == -1:
            return 0
        last = self.find_last_occurrences(target)
        return last - first + 1


searcher = Searcher([1, 3, 5, 5, 5, 7, 9])
print(searcher.binary_search(5))
print(searcher.count_occurrences(5))