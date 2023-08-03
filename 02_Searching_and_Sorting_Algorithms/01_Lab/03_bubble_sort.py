# exam: 03. Bubble Sort
# judge: https://judge.softuni.org/Contests/Compete/Index/3461#2

# Bubble sort - simple, but inefficient algorithm
# - Swap to neighbor element when not in the order until sorted
# - Memory: O(1)
# - Time: O(n^2)
# - Stable: Yes

def bubble_sort(numbers):
    had_swap = True
    filled_cells = 0

    while had_swap:
        had_swap = False

        for idx in range(len(numbers) - 1 - filled_cells):

            if numbers[idx] > numbers[idx + 1]:
                numbers[idx], numbers[idx + 1] = numbers[idx + 1], numbers[idx]
                had_swap = True

        filled_cells += 1

    return ' '.join(str(x) for x in numbers)


nums = [int(x) for x in input().split()]
print(bubble_sort(nums))
