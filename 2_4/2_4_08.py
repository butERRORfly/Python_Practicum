def main():
    count = int(input())
    tup = {}
    for i in range(count):
        name = input()
        number = int(input())
        tup[name] = tup.get(name, 0) + sum(int(x) for x in str(abs(number)))

    answer = []
    maxi = -1438573461348591645
    for j in tup.keys():
        maxi = max(maxi, tup[j])
        if maxi == tup[j]:
            answer.append(j)

    print(answer[-1])


if __name__ == "__main__":
    main()
