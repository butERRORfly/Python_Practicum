from sys import stdin
from math import gcd


def find_all_gcd(stack):
    current = stack[0]
    for i in stack[1:]:
        current = gcd(current, i)
        if current == 1:
            break

    return current


def main():
    for i in stdin:
        numbers = list(map(int, i.strip().split()))
        gcd = find_all_gcd(numbers)

        print(gcd)


if __name__ == "__main__":
    main()
