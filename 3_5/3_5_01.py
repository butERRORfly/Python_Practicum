def main():
    from sys import stdin

    summa = 0
    for line in stdin:
        summa += sum(list(map(int, line.split())))

    print(summa)


if __name__ == '__main__':
    main()