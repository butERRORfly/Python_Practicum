from itertools import product


def main():
    counter = int(input())
    keys = [input().split('-') for _ in range(counter)]

    data = set()
    for p in product(*keys):
        data.add(''.join(p))

    for i in sorted(data):
        print(i)


if __name__ == '__main__':
    main()
