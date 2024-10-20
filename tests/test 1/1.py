# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# print(f'{num1} + {num2}^{num3} = {num1 + num2 ** num3}')


def main():
    num1, num2, num3 = [int(input()) for _ in range(3)]
    print(f'{num1} + {num2}^{num3} = {num1 + num2 ** num3}')


if __name__ == '__main__':
    main()