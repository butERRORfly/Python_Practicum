def main():
    num = int(input())

    def plural(num, base):
        s = ''
        while num != 0:
            s += str(num % base)
            num //= base
        s = s[::-1]
        return sum(int(x) for x in s)

    maxi_summ = 0
    maxi_base = []
    for base in range(10, 1, -1):
        maxi_summ = max(maxi_summ, plural(num, base))
        if plural(num, base) == maxi_summ:
            maxi_base.append(base)
    print(min(maxi_base))


if __name__ == "__main__":
    main()
