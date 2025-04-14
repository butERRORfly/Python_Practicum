def gcd(*numbers):
    numbers = list(numbers)
    numbers.sort()

    def q(num, deli):
        list_n = []
        for u in num:
            if u % deli == 0:
                list_n.append(u)
        if len(list_n) == len(num):
            return 1
        else:
            return -1

    list_del = []
    for j in numbers:
        for i in range(1, numbers[-1] + 1):
            if q(numbers, i) == 1:
                list_del.append(i)

    return max(list_del)
