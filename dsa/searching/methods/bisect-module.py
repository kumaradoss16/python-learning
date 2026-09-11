import bisect

sorted_data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

index = bisect.bisect_left(sorted_data, 23)   # bisect_left() → find the correct insertion position
print(index)


# Check if the value actually exists at that position
def contains(sorted_arr, target):
    index = bisect.bisect_left(sorted_arr, target)
    return index < len(sorted_arr) and sorted_arr[index] == target


print(contains(sorted_data, 23))
print(contains(sorted_data, 24))

bisect.insort(sorted_data, 30)
print(sorted_data)