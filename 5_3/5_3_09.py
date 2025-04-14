import re


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def username_validation(name) -> str:
    pattern = r"^[a-zA-Z0-9_]+$"

    if not isinstance(name, str):
        raise TypeError

    if not re.match(pattern, name):
        raise BadCharacterError

    if name[0].isdigit():
        raise StartsWithDigitError

    return name


def name_validation(user_data) -> str:
    if not isinstance(user_data, str):
        raise TypeError

    if not all('а' <= char <= 'я' or char == 'ё' or char == ' ' for char in user_data.lower()):
        raise CyrillicError

    if not user_data.istitle():
        raise CapitalError

    return user_data


def user_validation(*args, **kwargs):
    records = ['last_name', 'first_name', 'username']

    try:
        if any([kwargs[x] == '' for x in records]):
            raise KeyError
    except Exception:
        raise KeyError

    if not all([x in records for x in kwargs.keys()]):
        raise KeyError

    name_validation(kwargs['last_name'])
    name_validation(kwargs['first_name'])
    username_validation(kwargs['username'])

    return kwargs
