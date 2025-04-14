import math

def main():
    N, M = map(int, input().split())

    total = math.comb(N, M)
    favorable = math.comb(N - 1, M - 1)

    print(favorable, total)


if __name__ == '__main__':
    main()