def main():
    file1, file2 = [input() for _ in range(2)]

    with open(file1, 'r') as f:
        line = f.readlines()

        data = []
        for i in line:
            data.append(i.strip().replace('\t', '').split())

    with open(file2, 'w') as f:
        for i in data:
            if len(i) != 0:
                f.write(f'{" ".join(i)}\n')


if __name__ == '__main__':
    main()
