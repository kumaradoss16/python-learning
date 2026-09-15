def search_rotated_array(arr,target):
    low, high = 0,len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid

        if arr[low] <= arr[mid]:
            if arr[low] < target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        else:
            if arr[mid] < target < arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1

rotated = [15, 18, 2, 3, 6, 12]
print(search_rotated_array(rotated, 6))
print(search_rotated_array(rotated, 100))