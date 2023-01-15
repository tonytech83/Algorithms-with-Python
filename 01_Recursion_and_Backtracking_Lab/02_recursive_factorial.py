def calc_factorial(n):
    """
    Recursive func which calculates factorial of n.

    :param n: integer
    :return: factorial of n
    """
    # BASE CASE - when n = 1
    if n == 1:
        return 1
    return n * calc_factorial(n - 1)


n = int(input())

print(calc_factorial(n))
