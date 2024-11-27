def make_equation(*numbers):
    if len(numbers) > 1:
        return f'({make_equation(*numbers[:-1:])}) * x + {numbers[-1]}'
    return numbers[0]