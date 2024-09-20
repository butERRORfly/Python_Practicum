def main():
    num = int(input())
    min_num = min(int(x) for x in str(num))
    max_num = max(int(x) for x in str(num))
    num_without = str(num).replace(str(min_num), "", 1).replace(str(max_num), "", 1)
    if min_num + max_num == int([x for x in str(num) if x in num_without][0]) * 2:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()