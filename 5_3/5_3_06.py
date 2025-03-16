def is_fraction(*num):
    if not all(type(x) in (int, float) for x in list(num)):
        raise TypeError


class NoSolutionsError(Exception):
    def __init__(self, message):
        super().__init__(message)


class InfiniteSolutionsError(Exception):
    def __init__(self, message):
        super().__init__(message)


def find_roots(a, b, c):
    is_fraction(a, b, c)

    if a == b == 0 and c != 0:
        raise NoSolutionsError('Вызвано исключение NoSolutionsError')

    elif a == b == c == 0:
        raise InfiniteSolutionsError('Вызвано исключение InfiniteSolutionsError')

    elif a == 0 and b != 0 and c != 0:
        return float(f'{-c / b:.2f}')
    elif (b ** 2 - 4 * a * c) < 0:
        raise NoSolutionsError('Вызвано исключение NoSolutionsError')
    else:
        dis = (b ** 2 - 4 * a * c)
        answer = sorted([float(((-b) + (dis ** 0.5)) / (2 * a)), float(((-b) - (dis ** 0.5)) / (2 * a))])
        return answer[0], answer[-1]
