from itertools import product, permutations


def main():
    a = input()
    b = input()

    suits = {
        'буби': 'бубен',
        'пики': 'пик',
        'трефы': 'треф',
        'черви': 'червей'
    }

    nominalo = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
    nominalo.remove(b)

    cards = list(product(nominalo, suits.values()))

    filtered_permutations = (perm for perm in permutations(cards, 3) if suits[a] in {card[1] for card in perm})

    for i, perm in enumerate(sorted(filtered_permutations)):
        if i >= 10:
            break
        print(', '.join(f'{nominal} {suit}' for nominal, suit in perm))


if __name__ == "__main__":
    main()