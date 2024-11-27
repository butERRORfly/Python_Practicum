def recursive_sum(*numbers):
    while numbers:
        return numbers[0] + recursive_sum(*numbers[1::])
    return 0
