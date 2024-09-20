def main():
    num = int(input())
    digits = sorted([int(x) for x in str(num)], reverse=True)
    if digits[-1] != 0:
        print(f'{digits[2]}{digits[1]} {digits[0]}{digits[1]}')
    else:
        print(f'{digits[1]}{digits[-1]} {digits[0]}{digits[1]}')


if __name__ == '__main__':
    main()