def merge(tuple1, tuple2):
    merger = []
    indexTuple1 = 0
    indexTuple2 = 0

    while indexTuple1 < len(tuple1) and indexTuple2 < len(tuple2):
        if tuple1[indexTuple1] < tuple2[indexTuple2]:
            merger.append(tuple1[indexTuple1])
            indexTuple1 += 1
        else:
            merger.append(tuple2[indexTuple2])
            indexTuple2 += 1

    merger.extend(tuple1[indexTuple1:])
    merger.extend(tuple2[indexTuple2:])

    return tuple(merger)
