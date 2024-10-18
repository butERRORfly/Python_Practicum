from itertools import product as porno


def main():
    suits = ['пик', 'треф', 'бубен', 'червей']
    elder = ['валет', 'дама', 'король', 'туз']
    juniors = [x for x in range(2, 11)]

    list_juniors = list(porno(juniors, suits))
    list_elder = list(porno(elder, suits))

    bad = input()
    for i in list_juniors:
        if bad not in i:
            print(f'{i[0]} {i[1]}')

    for i in list_elder:
        if bad not in i:
            print(f'{i[0]} {i[1]}')


if __name__ == "__main__":
    main()
