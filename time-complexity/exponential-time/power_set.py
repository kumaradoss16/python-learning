def subsets(nums, index, current):

    if index == len(nums):
        print(current)
        return

    subsets(nums, index + 1, current)
    subsets(nums, index + 1, current + [nums[index]])

numbers = [1, 2, 3]
subsets(numbers, 0, [])