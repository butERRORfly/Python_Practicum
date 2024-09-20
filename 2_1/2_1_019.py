def main():
    point = input()
    price = int(input())
    weight = int(input())
    count_of_money = int(input())

    print('================Чек================')
    print(f'Товар:{point:>29}')
    print(f'Цена:{str(weight) + "кг * " + str(price) + "руб/кг":>30}')
    print(f'Итого:{price * weight:>26}руб')
    print(f'Внесено:{count_of_money:>24}руб')
    print(f'Сдача:{count_of_money - (price * weight):>26}руб')
    print('=' * 35)

if __name__ == '__main__':
    main()