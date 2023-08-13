def sum_finder(target, numbers, current):
    current_sum = sum(current)

    if current_sum <= target and current_sum:
        print(' '.join(str(x) for x in current))

    if current_sum > target:
        return

    for idx in range(len(numbers)):
        num = numbers[idx]
        remaining = numbers[idx + 1:]
        sum_finder(target, remaining, current + [num])


numbers = [int(x) for x in input().split(', ')]
target = int(input())

sum_finder(target, numbers, [])
