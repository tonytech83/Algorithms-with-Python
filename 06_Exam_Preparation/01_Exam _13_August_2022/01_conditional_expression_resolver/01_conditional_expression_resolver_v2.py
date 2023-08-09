"""
exam: 01. Conditional Expression Resolver
judge: https://judge.softuni.org/Contests/Practice/Index/3592#0

Using recursion
"""


def parse_expression(expression, index):
    if expression[index].isdigit():
        return expression[index]

    if expression[index] == 't':
        return parse_expression(expression, index + 2)

    cursor = index + 2
    conditional_statements_counter = 0
    while True:
        symbol = expression[cursor]

        if symbol == '?':
            conditional_statements_counter += 1
        elif symbol == ':':
            if conditional_statements_counter == 0:
                return parse_expression(expression, cursor + 1)
            conditional_statements_counter -= 1
        cursor += 1


expression = input().split()
print(parse_expression(expression, 0))
