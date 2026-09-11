def ternary_search(arr, target):
    low = 0
    high  = len(arr) - 1

    while low <= high:
        third = (high - low) // 3
        mid1 = low + third
        mid2 = high - third

        if arr[mid1] == target:
            return mid1

        if arr[mid2] == target:
            return mid2

        if target < arr[mid1]:
            high = mid1 - 1

        if target > arr[mid2]:
            low = mid2 + 1

        else:
            low = mid1 + 1
            high = mid2 - 1

    return -1

arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(ternary_search(arr, 70))