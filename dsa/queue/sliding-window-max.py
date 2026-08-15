from collections import deque

def sliding_window_max(nums, k):
    result = []
    window = deque()

    for i, num in enumerate(nums):
        # Check expired index
        if window and window[0] <= i - k:
            window.popleft()

        # Remove the smaller values
        while window and nums[window[-1]] < num:
            window.pop()

        window.append(i)

        # check whether window is complete
        if i >= k - 1:
            result.append(nums[window[0]])

    return result

print(sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))
