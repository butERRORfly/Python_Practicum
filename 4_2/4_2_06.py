records = {
    'Эспрессо': {'coffee': 1},
    'Капучино': {"coffee": 1, "milk": 3},
    'Макиато': {"coffee": 2, "milk": 1},
    'Кофе по-венски': {"coffee": 1, "cream": 2},
    'Латте Макиато': {"coffee": 1, "milk": 2, "cream": 1},
    'Кон Панна': {"coffee": 1, "cream": 1}
}


def order(*orders):
    global records, in_stock

    for i in orders:
        if all(j in in_stock and records[i][j] <= in_stock[j] for j in records[i]):
            for k, v in records[i].items():
                in_stock[k] -= v
            return i
    return "К сожалению, не можем предложить Вам напиток"
