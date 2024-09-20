def main():
    num1 = int(input())
    num2 = int(input())
    digit1 = ((num1 % 10) + (num2 % 10)) % 10
    digit2 = ((num1 // 10 % 10) + (num2 // 10 % 10)) % 10
    digit3 = ((num1 // 100) + (num2 // 100)) % 10
    print(f'{digit3}{digit2}{digit1}')

if __name__ == '__main__':
    main()