def only_positive_even_sum(num1, num2):
    if not all([isinstance(x, int) for x in [num1, num2]]):
        raise TypeError
    if not all(isinstance(x, int) and x % 2 == 0 and x > 0 for x in [num1, num2]):
        raise ValueError
    return num1 + num2
