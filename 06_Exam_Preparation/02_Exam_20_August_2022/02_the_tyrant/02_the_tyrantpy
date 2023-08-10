"""
exam: 02. The Tyrant
judge: https://judge.softuni.org/Contests/Practice/Index/3623#1
"""


def calculate_min_sum(numbers):
    n = len(numbers)
    if n < 5:
        return min(numbers)

    dp = [0] * n
    for idx in range(4):
        dp[idx] = numbers[idx]

    for i in range(4, n):
        dp[i] = min(dp[i - 4:i]) + numbers[i]

    return min(dp[-4:])


nums = [int(x) for x in input().split()]

print(calculate_min_sum(nums))
