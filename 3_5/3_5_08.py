def main():
    file1, file2, file3 = [input() for _ in range(3)]

    data1 = set()
    with open(file1, 'r') as f:
        line = f.readlines()
        for i in line:
            i = i.split()
            for j in i:
                data1.add(j)

    data2 = set()
    with open(file2, 'r') as f:
        line = f.readlines()
        for i in line:
            i = i.split()
            for j in i:
                data2.add(j)

    data = data1 ^ data2
    with open(file3, 'w') as f:
        for i in sorted(data):
            f.write(f'{i}\n')


if __name__ == '__main__':
    main()
