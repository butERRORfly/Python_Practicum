records = []


def enter_results(*numbers):
    global records
    records.extend(list(numbers))


def get_sum():
    sumEvens = round(sum([records[x] for x in range(len(records)) if x % 2 == 0]), 2)
    sumOdds = round(sum([records[x] for x in range(len(records)) if x % 2 != 0]), 2)
    return sumEvens, sumOdds


def get_average():
    evensLenList = len([records[x] for x in range(len(records)) if x % 2 == 0])
    oddsLenList = len([records[x] for x in range(len(records)) if x % 2 != 0])
    averageEvens = round(sum([records[x] for x in range(len(records)) if x % 2 == 0]) / evensLenList, 2)
    averageOdds = round(sum([records[x] for x in range(len(records)) if x % 2 != 0]) / oddsLenList, 2)
    return averageEvens, averageOdds
