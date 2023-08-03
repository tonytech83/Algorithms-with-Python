# exam: 04. Insertion Sort
# judge: https://judge.softuni.org/Contests/Compete/Index/3461#3

# Insertion sort - simple, but inefficient algorithm
# - Move the first unsorted element left to its place
# - Memory: O(1)
# - Time: O(n^2)
# - Stable: Yes
# - Method: Insertion


def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        for j in range(i, 0, -1):
            if numbers[j] < numbers[j - 1]:
                numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
            # when else we do not need to check next number
            else:
                break

    return ' '.join(str(x) for x in numbers)


nums = [int(x) for x in input().split()]
print(insertion_sort(nums))
