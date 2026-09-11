def binary_search_insert(arr, value):
    low = 0
    high = len(arr)

    # Find the correct insertion position
    while low < high:
        mid = (low + high) // 2

        if arr[mid] < value:
            low = mid + 1
        else:
            high = mid

    arr.insert(low, value)


numbers = [10, 20, 30, 40, 50]
print("Before:", numbers)
binary_search_insert(numbers, 35)
print("After:", numbers)