import re


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(name) -> str:
    """Валидация имени пользователя"""

    pattern = r"^[a-zA-Z0-9_]+$"

    if not isinstance(name, str):
        raise TypeError

    if not re.match(pattern, name):
        raise BadCharacterError

    if name[0].isdigit():
        raise StartsWithDigitError

    return name
