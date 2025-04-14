from itertools import product

OPERATORS = {
    'not': 'not',
    'and': 'and',
    'or': 'or',
    '^': '!=',
    '->': '<=',
    '~': '==',
}

PRIORITY = {
    'not': 3,
    'and': 2,
    'or': 1,
    '^': 4,
    '->': 0,
    '~': 0,
    '(': -1,
}


def parse_expression(expression):
    stack = []
    output = []
    expression = expression.replace('(', ' ( ').replace(')', ' ) ')

    for token in expression.split():
        if token.isupper():  # If the token is a variable
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Pop the '('
        elif token in OPERATORS:
            while (stack and PRIORITY.get(token, -1) <= PRIORITY.get(stack[-1], -1)):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output


def evaluate(expression, variables):
    stack = []
    for token in expression:
        if token.isupper():
            stack.append(variables[token])
        elif token == 'not':
            stack.append(not stack.pop())
        else:
            right = stack.pop()
            left = stack.pop()
            if token == 'and':
                stack.append(left and right)
            elif token == 'or':
                stack.append(left or right)
            elif token == '^':
                stack.append(left != right)
            elif token == '->':
                stack.append(not left or right)
            elif token == '~':
                stack.append(left == right)

    return int(stack.pop())


def main():
    expression = input()
    variables = sorted(set(filter(str.isupper, expression)))
    parsed_expression = parse_expression(expression)
    table = product([0, 1], repeat=len(variables))

    print(*variables, 'F')
    for values in table:
        globals_ = {key: bool(value) for key, value in zip(variables, values)}
        result = evaluate(parsed_expression, globals_)
        print(*values, result)


if __name__ == "__main__":
    main()