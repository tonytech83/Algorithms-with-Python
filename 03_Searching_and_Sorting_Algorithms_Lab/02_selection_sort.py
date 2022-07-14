numbers = [int(x) for x in input().split()]

for idx in range(len(numbers)):
    min_number = numbers[idx]
    min_idx = idx

    # walk through all elements from left to right till end of array
    for next_idx in range(idx + 1, len(numbers)):
        next_number = numbers[next_idx]
        if next_number < min_number:
            min_number = next_number
            min_idx = next_idx

    # swap the numbers
    numbers[idx], numbers[min_idx] = numbers[min_idx], numbers[idx]

print(*numbers, sep=' ')
