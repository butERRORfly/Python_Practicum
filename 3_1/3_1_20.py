def main():
    stroke = list(map(str, input().split()))

    def fac(n):
        if n == 1:
            return 1
        return fac(n - 1) * n

    numbers = []
    for i in stroke:
        if i.isdigit():
            numbers.append(int(i))
        elif i in '+-*/':
            match i:
                case '+':
                    numbers.append(numbers.pop(-2) + numbers.pop(-1))
                case '-':
                    numbers.append(numbers.pop(-2) - numbers.pop(-1))
                case '*':
                    numbers.append(numbers.pop(-2) * numbers.pop(-1))
                case '/':
                    numbers.append(int(numbers.pop(-2) // numbers.pop(-1)))
        elif i in '~#!':
            match i:
                case '~':
                    numbers.append(- numbers.pop(-1))
                case '#':
                    numbers.append(numbers[-1])
                case '!':
                    numbers.append(fac(numbers.pop(-1)))
        elif i == '@':
            _1 = numbers.pop(-3)
            numbers.append(_1)
        else:
            raise Exception

    else:
        print(*numbers)


if __name__ == "__main__":
    main()
