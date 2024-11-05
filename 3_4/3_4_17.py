from itertools import product, combinations


def main():
    a = input()
    b = input()
    prev = input()

    suits = {
        'буби': 'бубен',
        'пики': 'пик',
        'трефы': 'треф',
        'черви': 'червей'
    }

    nominalo = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
    nominalo.remove(b)

    cards = list(product(nominalo, suits.values()))

    filtered_permutations = (perm for perm in combinations(cards, 3) if suits[a] in {card[1] for card in perm})

    flag = 0
    for i, perm in enumerate(sorted(filtered_permutations)):
        match flag:
            case 1:
                print(', '.join(f'{nominal} {suit}' for nominal, suit in perm))
                break
        match ', '.join(f'{nominal} {suit}' for nominal, suit in perm) == prev:
            case 1:
                flag = 1


if __name__ == "__main__":
    main()
