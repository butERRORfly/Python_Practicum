def main():
    N, M = [int(input()) for _ in range(2)]

    dic = {}
    for i in range(N):
        enjoyer = input()
        dic[enjoyer] = dic.get(enjoyer, 0) + 1

    for _ in range(M):
        enjoyer = input()
        dic[enjoyer] = dic.get(enjoyer, 0) + 1

    counter = 0
    for i in dic.items():
        if i[-1] == 1:
            counter += 1

    if counter != 0:
        print(counter)
    else:
        print('Таких нет')


if __name__ == "__main__":
    main()
