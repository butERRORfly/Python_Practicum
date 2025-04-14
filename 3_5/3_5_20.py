def main():
    summa = 0
    with open('numbers.num', 'rb') as f:
        while char := f.read(2):
            summa += int.from_bytes(char)

    print(summa % 0x10000)


if __name__ == '__main__':
    main()
