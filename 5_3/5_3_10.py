import string
from hashlib import sha256


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def password_validation(password, min_length=8, possible_chars=string.ascii_letters + string.digits,
                        at_least_one=str.isdigit) -> str:
    if not isinstance(password, str):
        raise TypeError
    if len(password) < min_length:
        raise MinLengthError
    if any([char not in possible_chars for char in password]):
        raise PossibleCharError
    if not any([at_least_one(x) for x in password]):
        raise NeedCharError

    hash_object = sha256()
    hash_object.update(password.encode())
    return hash_object.hexdigest()
