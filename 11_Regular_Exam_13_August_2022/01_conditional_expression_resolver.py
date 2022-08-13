line_from_input = input()


def resolve_expression(expression):
    if '?' not in expression:
        return expression

    bool_val, choices = expression.split('?', 1)
    true, false = choices.rsplit(':', 1)
    bool_val = bool_val.strip()

    if bool_val == 't':
        return resolve_expression(true)
    if bool_val == 'f':
        return resolve_expression(false)


print(resolve_expression(line_from_input))
