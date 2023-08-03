# exam: 05. Quicksort
# judge: https://judge.softuni.org/Contests/Compete/Index/3461#4

# QuickSort - Efficient sorting algorithm
# - Choose a pivot; move smaller elements left and larger right; sort left and right
# - Memory: O(log(n)) -> stack space (recursion)
# - Time: O(n^2) -> When the pivot element divides the array into two unbalanced sub-arrays (huge difference in size)
# - Stable: Depends
# - Method: Partitioning

def quick_sort(start, end, nums):
    if start >= end:
        return

    pivot_idx = start
    left_idx = start + 1
    right_idx = end

    while left_idx <= right_idx:
        if nums[left_idx] > nums[pivot_idx] > nums[right_idx]:
            nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]

        if nums[left_idx] <= nums[pivot_idx]:
            left_idx += 1

        if nums[right_idx] >= nums[pivot_idx]:
            right_idx -= 1

    nums[pivot_idx], nums[right_idx] = nums[right_idx], nums[pivot_idx]

    quick_sort(start, right_idx - 1, nums)
    quick_sort(left_idx, end, nums)


nums = [int(x) for x in input().split()]
quick_sort(0, len(nums) - 1, nums)
print(*nums, sep=' ')
