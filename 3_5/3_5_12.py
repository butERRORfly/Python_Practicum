def main():
    file1, file2, file3, file4 = [input() for _ in range(4)]

    with open(file1, 'r') as f:
        lines = f.readlines()

        data = []
        for line in lines:
            data.append(line.split())

    for line in data:
        even, odd, eq = [], [], []
        for num in line:
            if len([x for x in num if x in '02468']) > len([x for x in num if x not in '02468']):
                even.append(num)
            elif len([x for x in num if x in '02468']) < len([x for x in num if x not in '02468']):
                odd.append(num)
            else:
                eq.append(num)

        with open(file2, 'a') as f:
            f.write(' '.join(even) + '\n')

        with open(file3, 'a') as f:
            f.write(' '.join(odd) + '\n')

        with open(file4, 'a') as f:
            f.write(' '.join(eq) + '\n')


if __name__ == '__main__':
    main()
