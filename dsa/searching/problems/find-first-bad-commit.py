def find_first_bad_commit(n, is_bad):
    low, high = 1, n
    while low < high:
        mid = (low + high) // 2
        if is_bad(mid):
            high = mid
        else:
            low = mid + 1

    return low


def is_bad_simulation(commit):
    return commit >= 6


print(find_first_bad_commit(10, is_bad_simulation))