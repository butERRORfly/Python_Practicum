from itertools import permutations


def main():
    list_names = []
    for i in range(int(input())):
        name = input()
        list_names.append(name)

    for i in sorted(permutations(list_names, 3)):
        print(', '.join(i))


if __name__ == "__main__":
    main()
