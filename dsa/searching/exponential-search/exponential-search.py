
def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def exponential_search(arr, target):
    n = len(arr)
    if n == 0:
        return -1
    if arr[0] == target:
        return 0

    # Finding a range by doubling - 1, 2, 4, 8, ....
    bound = 1
    while bound < n and arr[bound] < target:
        bound *= 2

    # Binary search within the found range
    low = bound // 2
    high = bound + 1

    return binary_search_iterative(arr[low: high], target) + low if binary_search_iterative(arr[low: high], target) != -1 else -1

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
print(exponential_search(arr, 22))


