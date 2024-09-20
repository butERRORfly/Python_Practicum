def main():
    where = input()
    x, y = 0, 0
    while where != 'СТОП':
        count = int(input())
        if where == 'СЕВЕР':
            y += count
        if where == 'ВОСТОК':
            x += count
        if where == 'ЮГ':
            y += -count
        if where == 'ЗАПАД':
            x += -count
        where = input()

    print(f'{y}\n{x}')

if __name__ == '__main__':
    main()