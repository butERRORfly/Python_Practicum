def main():
    count_of_apples_for_petya = int(input())
    count_of_apples_for_vasya = int(input())

    petya = 7 - 3 + 2 + count_of_apples_for_petya
    vasya = 6 + 3 + 5 - 2 + count_of_apples_for_vasya

    if petya > vasya:
        print('Петя')
    else:
        print('Вася')

if __name__ == '__main__':
    main()