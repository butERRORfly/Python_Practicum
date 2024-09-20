def main():
    a = float(input())
    b = float(input())
    c = float(input())

    if a == b == 0 and c != 0:
        print('No solution')
    elif a == b == c == 0:
        print('Infinite solutions')
    elif a == 0 and b != 0 and c != 0:
        print(float(f'{-c / b:.2f}'))
    elif (b ** 2 - 4 * a * c) < 0:
        print('No solution')
    elif (b ** 2 - 4 * a * c) == 0:
        print(f'{(-b) / 2 * a:.2f}')
    else:
        dis = (b ** 2 - 4 * a * c)
        answer = sorted([float(((-b) + (dis ** 0.5)) / (2 * a)), float(((-b) - (dis ** 0.5)) / (2 * a))])
        print(*[f'{x:.2f}' for x in answer])

if __name__ == '__main__':
    main()