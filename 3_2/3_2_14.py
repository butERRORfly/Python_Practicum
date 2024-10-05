def main():
    menu = set()
    for _ in range(int(input())):
        enjoy = input()
        menu.add(enjoy)

    recipes = {}
    for _ in range(int(input())):
        recipe = input()
        for _ in range(int(input())):
            product = input()
            recipes[recipe] = recipes.get(recipe, []) + [product]

    answer = []
    for i in recipes.keys():
        if set(recipes[i]).issubset(menu):
            answer.append(i)

    if len(answer) != 0:
        print('\n'.join(sorted(answer)))
    else:
        print('Готовить нечего')

if __name__ == '__main__':
    main()
