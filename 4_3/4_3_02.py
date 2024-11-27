def recursive_digit_sum(integer):
    if len(str(integer)) == 0:
        return 0
    return int(str(integer)[-1]) + recursive_digit_sum(str(integer)[:-1:])
