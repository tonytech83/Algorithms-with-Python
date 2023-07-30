# exam: 02. Recursive Factorial
# judge: https://judge.softuni.org/Contests/Compete/Index/3459#1

def factorial(n):
    """
    Simple function for calculation factorial of n with recursion

    :param n: integer
    :return: factorial of n
    """
    # BASE CASE - factorial of 0 is constant and equal to 1
    if n == 0:
        return 1
    # Recursive call
    return n * factorial(n - 1)


print(factorial(int(input())))
