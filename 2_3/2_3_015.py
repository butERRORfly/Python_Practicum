def main():
    count = int(input())
    counter = 0
    for i in range(count):
        rabbit = input()
        if 'зайка' in rabbit:
            counter += 1
    print(counter)


if __name__ == '__main__':
    main()