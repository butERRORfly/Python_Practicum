def is_prime(num):
    listDel = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            listDel.append(i)
            listDel.append(num // i)

    listDel = sorted(list(set(listDel)))
    return True if len(listDel) <= 2 else False