def main():
    text = []
    while string := input():
        text.append(string)

    records = {}
    for i in text:
        i = i.split(' ')
        for word in i:
            records[len(word)] = records.get(len(word), []) + sorted(
                list(set(([x.upper() for x in i if len(x) == len(word)]))))

    for i in records.keys():
        records[i] = sorted(list(set(records[i])), reverse=True)
        print(f'{i}: {"; ".join(records[i])}')


if __name__ == '__main__':
    main()
