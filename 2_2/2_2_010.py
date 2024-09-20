def main():
    num = int(input())
    step1 = sum(int(x) for x in str(num)[:-1:])
    step2 = int(str(num)[1]) + int(str(num)[-1])
    print(f'{max(step1, step2)}{min(step1, step2)}')


if __name__ == '__main__':
    main()