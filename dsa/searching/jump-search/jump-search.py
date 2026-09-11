import math

def jump_search(arr, target):
    n = len(arr)
    block_size = int(math.sqrt(n))

    block_start = 0
    while block_start < n and arr[min(block_start + block_size, n) - 1] < target:
        block_start += block_size


    for i in range(block_start, min(block_size + block_start, n)):
        if arr[i] == target:
            return i

    return -1



arr = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60]
print(jump_search(arr, 32))