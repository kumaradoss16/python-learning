def next_greater_element(nums):
    result = [-1] *  len(nums)
    stack = []   # Stores indices

    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    return result


print(next_greater_element([2, 1, 2, 4, 3]))


