class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(user_data) -> str:
    if not isinstance(user_data, str):
        raise TypeError

    if not all('а' <= char <= 'я' or char == 'ё' or char == ' ' for char in user_data.lower()):
        raise CyrillicError

    if not user_data.istitle():
        raise CapitalError

    return user_data
