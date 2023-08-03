# exam: 07. Recursive Fibonacci
# judge: https://judge.softuni.org/Contests/Compete/Index/3459#6

# This didn't work in judge!!!
def calc_fib(number):
    if number <= 1:
        return 1
    return calc_fib(number - 1) + calc_fib(number - 2)


# def calc_fib(number):
#     num1 = 1
#     num2 = 1
#     result = 0
#
#     for num in range(number - 1):
#         result = num1 + num2
#         num1, num2 = num2, result
#
#     return result
#
#
# n = int(input())
# print(calc_fib(n))
