records = []


def add_number(number):
    records.append(str(number))


def get_prod():
    res = 1
    for i in records:
        res *= int(i)
    return f"{' * '.join(records)} = {res}"
