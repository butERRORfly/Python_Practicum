from itertools import permutations


def main():
    num = int(input())
    _set = set()
    for i in range(num):
        want = input().split(', ')
        for j in want:
            _set.add(j)

    _set = sorted(_set)

    for i in sorted(permutations(_set, 3)):
        print(*i)


if __name__ == "__main__":
    main()
