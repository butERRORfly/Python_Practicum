def main():
    num1 = int(input())
    num2 = int(input())

    list_del = []
    for i in range(1, num1 * num2 + 1):
        if i % num1 == 0 and i % num2 == 0:
            list_del.append(i)

    print(min(list_del))

if __name__ == '__main__':
    main()