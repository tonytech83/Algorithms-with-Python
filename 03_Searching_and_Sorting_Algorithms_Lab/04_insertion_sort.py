nums = [int(x) for x in input().split()]

for i in range(1, len(nums)):
    for j in range(i, 0, -1):
        # compair the numbers and if True, swap them
        if nums[j] < nums[j - 1]:
            # if True -> swap the numbers
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
        # when False, we have less iteration if we have sorted sub set
        else:
            break

print(*nums, sep=' ')
