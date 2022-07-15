def quick_sort(start_idx, end_idx, nums):
    # base case
    if start_idx >= end_idx:
        return
    pivot = start_idx
    left = start_idx + 1
    right = end_idx

    while left <= right:
        if nums[left] > nums[pivot] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left] <= nums[pivot]:
            left += 1
        if nums[right] >= nums[pivot]:
            right -= 1

    nums[pivot], nums[right] = nums[right], nums[pivot]
    # recursion
    quick_sort(start_idx, right - 1, nums)
    quick_sort(left, end_idx, nums)


nums = [int(x) for x in input().split()]

quick_sort(0, len(nums) - 1, nums)

print(*nums, sep=" ")
