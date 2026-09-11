# Linear search on Unsorted data
def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index

    return -1  # not found

arr = [4, 2, 7, 9, 1]
print(linear_search(arr, 7))
print(linear_search(arr, 5))