def main():
    num1 = int(input())
    num2 = int(input())

    list_del = []
    for i in range(1, max(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0 and i:
            list_del.append(i)

    print(max(list_del))

if __name__ == '__main__':
    main()