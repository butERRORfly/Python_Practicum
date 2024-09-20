def main():
    hh = 0
    answer = -1
    N = int(input())
    for i in range(N):
        block = int(input())
        h = block % 256
        r = (block // 256) % 256
        m = block // 256 ** 2
        fh = (37 * (m + r + hh)) % 256
        if fh != h or fh > 100:
            answer = i
            break
        hh = fh
    print(answer)

if __name__ == '__main__':
    main()