nums = [int(x) for x in input().split()]

is_sorted = False
filled_cells = 0

while not is_sorted:
    is_sorted = True

    for idx in range(1, len(nums) - filled_cells):
        if nums[idx] < nums[idx - 1]:
            # if True -> swap the numbers
            nums[idx], nums[idx - 1] = nums[idx - 1], nums[idx]
            is_sorted = False
    filled_cells += 1

print(*nums, sep=' ')
