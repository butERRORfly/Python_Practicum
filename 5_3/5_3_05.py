from collections.abc import Iterable


def is_iter(*collection):
    if not all(isinstance(x, Iterable) for x in list(collection)):
        raise StopIteration


def is_uniformity(*collection):
    records = []
    for i in collection:
        records.extend(list(i))

    first_type = type(records[0])
    if any(type(item) is not first_type for item in records):
        raise TypeError


def is_sorted(*collection):
    for i in collection:
        if list(i) != sorted(i):
            raise ValueError


def merge(iterable1, iterable2):
    is_iter(iterable1, iterable2)
    is_uniformity(iterable1, iterable2)
    is_sorted(iterable1, iterable2)
    merger = []
    i, j = 0, 0

    while i < len(iterable1) and j < len(iterable2):
        if iterable1[i] < iterable2[j]:
            merger.append(iterable1[i])
            i += 1
        else:
            merger.append(iterable2[j])
            j += 1

    merger.extend(iterable1[i:])
    merger.extend(iterable2[j:])

    return tuple(merger)
