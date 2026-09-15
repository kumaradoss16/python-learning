from collections import deque

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


def has_job_been_queued(job_queue, job_id):
    sorted_snapshot = sorted(job_queue)
    return binary_search_iterative(sorted_snapshot, job_id) != -1


printer_queue = deque([1050, 1002, 1023, 1042, 1010])
print(has_job_been_queued(printer_queue, 1042))
print(has_job_been_queued(printer_queue, 9999))


