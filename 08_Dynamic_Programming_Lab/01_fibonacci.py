def calc_fib(n, memo):
    # check if we already had n in dict memo
    if n in memo:
        return memo[n]
    # check if we already hit the bottom
    if n <= 2:
        return 1

    # if calc is not i our dict memo
    result = calc_fib(n - 1, memo) + calc_fib(n - 2, memo)
    # caching calculation, to have less calculation
    memo[n] = result
    return result


n = int(input())

print(calc_fib(n, {}))
