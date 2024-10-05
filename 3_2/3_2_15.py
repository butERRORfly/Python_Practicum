def main():
    def p1(lst):
        l_new = []
        for i in lst:
            l_new.append(bin(i)[2::])
        return l_new

    numbers = p1(list(map(int, input().split())))
    answer = []

    for i in numbers:
        answer.append({
            "digits": len(i),
            "units": i.count('1'),
            "zeros": i.count('0'),
        })

    print(answer)

if __name__ == '__main__':
    main()
