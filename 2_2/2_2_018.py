def main():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    list_num = sorted([num1, num2, num3], reverse=True)

    if list_num[0] ** 2 == list_num[1] ** 2 + list_num[2] ** 2:
        print('100%')

    if list_num[0] ** 2 < list_num[1] ** 2 + list_num[2] ** 2:
        print('крайне мала')

    if list_num[0] ** 2 > list_num[1] ** 2 + list_num[2] ** 2:
        print('велика')

if __name__ == '__main__':
    main()