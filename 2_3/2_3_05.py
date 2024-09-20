def main():
    price = float(input())
    summ = 0
    while price != 0:
        if price >= 500:
            summ += price * 0.9
        else:
            summ += price
        price = float(input())
    print(f'{summ:>01}')

if __name__ == '__main__':
    main()