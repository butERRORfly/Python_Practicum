from itertools import product


def main():
    alphabet = {i: chr(i) for i in range(65, 91)}
    string = input()

    variables = [x for x in string.split() if x in alphabet.values()]
    print(' '.join(sorted(set(variables))), 'F')

    for i in product([0, 1], repeat=len(set(variables))):
        eval_dict = dict(zip(sorted(set(variables)), i))
        result = eval(string, {}, eval_dict)

        print(*i, int(result))


if __name__ == "__main__":
    main()
