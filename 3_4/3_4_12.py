def main():
    string = []
    for _ in range(int(input())):
        string.extend(input().split(', '))

    print('\n'.join([f'{num}. {item}' for num, item in enumerate(sorted(string), 1)]))

if __name__ == "__main__":
    main()