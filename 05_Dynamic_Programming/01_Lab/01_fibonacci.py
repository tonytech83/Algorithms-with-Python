"""
exam: 01. Fibonacci
judge: https://judge.softuni.org/Contests/Practice/Index/3471#0

Recursive approach with dynamic programming (memorization)
"""


def calc_fib(n, memo):
    # check if we already had n in dict memo
    if n in memo:
        return memo[n]

    # BASE CASE - bottom of recursion
    if n <= 2:
        return 1

    # calc the fibonacci of n and add result in memo dict
    result = calc_fib(n - 1, memo) + calc_fib(n - 2, memo)
    memo[n] = result

    return result


n = int(input())

print(calc_fib(n, {}))
