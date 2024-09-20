def main():
    num = int(input())

    if str(num) == str(num)[::-1]:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()