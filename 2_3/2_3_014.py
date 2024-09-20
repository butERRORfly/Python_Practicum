def main():
    num = int(input())

    def delimitri(n):
        list_del = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                list_del.append(i)
                list_del.append(n // i)
        list_del.sort()
        list_del = list(set(list_del))
        return len(list_del)

    if delimitri(num) == 2:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()