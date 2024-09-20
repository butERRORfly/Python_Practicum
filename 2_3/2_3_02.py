def main():
    counter = 0
    adventure = input()
    while adventure != 'Приехали!':
        if 'зайка' in adventure:
            counter += 1
        adventure = input()
    print(counter)

if __name__ == '__main__':
    main()