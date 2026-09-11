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

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(binary_search_iterative(arr, 23))
print(binary_search_iterative(arr, 100))