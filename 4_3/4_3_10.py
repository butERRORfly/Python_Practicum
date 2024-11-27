def make_linear(numbers):
    records = []
    for el in numbers:
        if isinstance(el, int):
            records.append(el)
        else:
            records.extend(make_linear(el))
    return records
