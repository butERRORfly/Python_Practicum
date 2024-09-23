def main():
    def is_digit(num):
        list_num = []
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                list_num.append(i)
                list_num.append(num // i)
        list_num.sort()
        list_num = list(set(list_num))
        return len(list_num)

    counter = 0
    for i in range(int(input())):
        num = int(input())
        if is_digit(num) == 2:
            counter += 1
    print(counter)


if __name__ == "__main__":
    main()
