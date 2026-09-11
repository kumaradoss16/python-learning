def linear_search_sorted(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
        if value > target:    # we've gone past where target would be - stop early
            return -1

    return -1

arr = [1, 2, 4, 7, 9]
print(linear_search_sorted(arr, 4))
print(linear_search_sorted(arr, 5))
