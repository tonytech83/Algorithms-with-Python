# exam: 02. Selection Sort
# judge: https://judge.softuni.org/Contests/Compete/Index/3461#1

# Selection sort - simple, but inefficient algorithm
# - Swap the first element with the min element on the right, then the second, etc.
# - Memory: O(1)
# - Time: O(n^2)
# - Stable: No

def selection_sort(idx, numbers):
    while idx < len(numbers):

        num = numbers[idx]
        min_num = min(numbers[idx: len(numbers)])
        min_idx = numbers[idx: len(numbers)].index(min_num) + idx

        if num > min_num:
            numbers[idx], numbers[min_idx] = numbers[min_idx], numbers[idx]

        idx += 1

    return ' '.join(str(x) for x in numbers)


nums = [int(x) for x in input().split()]
print(selection_sort(0, nums))
