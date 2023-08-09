"""
exam: 01. Conditional Expression Resolver
judge: https://judge.softuni.org/Contests/Practice/Index/3592#0

Using regex
"""
import re

expression = input()
pattern = r'([tf]\s\?\s\d+\s\:\s\d+)'

while True:
    matches = re.findall(pattern, expression)

    if not matches:
        break

    condition, true_answer, false_answer = matches[0][0], matches[0][4], matches[0][-1]
    answer = true_answer if condition == 't' else false_answer
    expression = expression.replace(matches[0], answer)

print(expression)
