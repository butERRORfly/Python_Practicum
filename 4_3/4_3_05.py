def result_accumulator(oldFunc):
    records = []

    def newFunc(*args, method='accumulate', **kwargs):
        if method == 'accumulate':
            records.append(oldFunc(*args, **kwargs))
        elif method == 'drop':
            records.append(oldFunc(*args, **kwargs))
            answer = records[:]
            records.clear()
            return answer

    return newFunc
