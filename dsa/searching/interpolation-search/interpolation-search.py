def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        if arr[high] == arr[low]:
            if arr[low] == target:
                return low
            return -1

        position = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[position] == target:
            return position
        elif arr[position] < target:
            low = position + 1
        else:
            high = position - 1

    return -1

arr = [10, 20, 30, 40, 50, 60, 70, 75, 80, 90, 100]
print(interpolation_search(arr, 75))