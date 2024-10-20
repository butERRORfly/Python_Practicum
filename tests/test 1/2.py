def main():
    num1, num2 = [int(input()) for _ in range(2)]
    string = input()

    if len(string) % 6 == 0:
        print(num1 + num2)
    elif len(string) % 3 == 0:
        print(num1 - num2)
    elif len(string) % 2 == 0:
        print(num1 * num2)
    else:
        print(num1 // num2)


if __name__ == '__main__':
    main()