from itertools import product


def bunny(start, finish, length):
    result = []
    for i in product([-1, -3, 1, 3], repeat=length):
        if sum(i) == finish - start:
            path = []
            pos = start
            for j in i:
                pos += j
                path.append(pos)
            if len(path) == length and finish not in path[:-1]:
                result.append([start] + path)

    return result
