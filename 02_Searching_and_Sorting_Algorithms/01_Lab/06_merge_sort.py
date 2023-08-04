# exam: 06. Merge Sort
# judge: https://judge.softuni.org/Contests/Compete/Index/3461#5

# Merge sort - Efficient sorting algorithm
# - Divide the list into sub-lists (typically two sub-lists)
# - Sort each sub-list (recursively call merge-sort)
# - Merge the sorted sub-lists into a single list
# - Memory: O(n) / O(log(n)) -> two implementations
# - Time: O(n*log(n))
# - Stable: Yes
# - Method: Merging
# - Highly parallelizable on multiple cores / machines -> up to O(log(n))

def merge_arrays(left_array, right_array):
    result = []
    left_idx = 0
    right_idx = 0

    # append the element which is smaller from both arrays and
    # move the index of array from which we take an element
    while left_idx < len(left_array) and right_idx < len(right_array):
        if left_array[left_idx] < right_array[right_idx]:
            result.append(left_array[left_idx])
            left_idx += 1
        else:
            result.append(right_array[right_idx])
            right_idx += 1

    # takes remaining elements from left_array if any
    for idx in range(left_idx, len(left_array)):
        result.append(left_array[idx])

    # takes remaining elements from right_array if any
    for idx in range(right_idx, len(right_array)):
        result.append(right_array[idx])

    return result


# this implementation is O(log(n)) for memory
def merge_sort(nums):
    if len(nums) == 1:
        return nums

    # divide the list to two sub-lists
    mid_idx = len(nums) // 2
    left_array = nums[: mid_idx]
    right_array = nums[mid_idx:]

    # Recursive call
    return merge_arrays(merge_sort(left_array), merge_sort(right_array))


nums = [int(x) for x in input().split()]

print(*(merge_sort(nums)), sep=' ')
