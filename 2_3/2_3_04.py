def main():
    num1 = int(input())
    num2 = int(input())
    if num2 >= num1:
        for i in range(num1, num2 + 1):
            print(i, end=' ')
    else:
        for i in range(num1, num2 - 1, -1):
            print(i, end=' ')

if __name__ == '__main__':
    main()