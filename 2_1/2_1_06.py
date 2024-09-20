def main():
    name_of_point = input()
    price = int(input())
    weight = int(input())
    count_of_money = int(input())

    print("Чек")
    print(f'{name_of_point} - {weight}кг - {price}руб/кг')
    print(f'Итого: {int(price * weight)}руб')
    print(f'Внесено: {count_of_money}руб')
    print(f'Сдача: {count_of_money - int(price * weight)}руб')

if __name__ == '__main__':
    main()