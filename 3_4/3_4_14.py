from itertools import permutations


def main():
    list_names = []
    num = int(input())
    for i in range(num):
        name = input()
        list_names.append(name)

    for i in sorted(permutations(list_names, 3)):
        print(', '.join(i))


if __name__ == "__main__":
    main()
