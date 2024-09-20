def main():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    if max(num1, num2, num3) < (num1 + num2 + num3) - max(num1, num2, num3):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()