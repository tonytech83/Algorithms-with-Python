# exam: 03. Bubble Sort
# judge: https://judge.softuni.org/Contests/Compete/Index/3461#2

nums = [int(x) for x in input().split()]

for i in range(len(nums)):
    for j in range(len(nums) - 1 - i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(*nums, sep=' ')
