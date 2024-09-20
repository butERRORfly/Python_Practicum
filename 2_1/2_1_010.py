def main():
    name = input()
    locker = input()

    print(f'Группа №{locker[0]}.')
    print(f'{locker[-1]}. {name}.')
    print(f'Шкафчик: {locker}.')
    print(f'Кроватка: {locker[1]}.')

if __name__ == '__main__':
    main()