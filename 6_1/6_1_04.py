def main():
    numbers = list(map(float, input().split()))
    result = 1.0
    for i in numbers:
        result *= i
    print(result ** (1.0 / len(numbers)))


if __name__ == '__main__':
    main()
