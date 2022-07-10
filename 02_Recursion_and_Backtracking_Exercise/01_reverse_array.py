def reversed_array(idx, numbers):
    # Base case - check for end on massive
    if idx == len(numbers) // 2:
        return

    swap_idx = len(numbers) - 1 - idx
    keep_number = numbers[idx]  # numbers[idx], numbers[swap_idx] = numbers[swap_idx], numbers[idx]
    numbers[idx] = numbers[swap_idx]
    numbers[swap_idx] = keep_number
    # recursion
    reversed_array(idx + 1, numbers)


numbers = input().split()
reversed_array(0, numbers)

print(" ".join(numbers))
