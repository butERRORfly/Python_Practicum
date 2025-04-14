def main():
    with open(input(), 'r') as f:
        lines = f.readlines()

        data = []
        for i in lines:
            i = i.split()
            i = [int(x) for x in i]

            data += i

    print(len(data))
    print(len([x for x in data if x > 0]))
    print(min(data))
    print(max(data))
    print(sum(data))
    print(f'{(sum(data) / len(data)):.2f}')


if __name__ == '__main__':
    main()
