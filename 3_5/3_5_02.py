from sys import stdin


def main():
    summa = 0
    counter = 0
    for line in stdin:
        summa += int(line.split()[-1]) - int(line.split()[-2])
        counter += 1

    print(round(summa / counter))


if __name__ == '__main__':
    main()
