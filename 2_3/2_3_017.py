def main():
    num = int(input())
    num = str(num)
    for i in num:
        if int(i) % 2 == 0:
            num = num.replace(i, '')
    print(int(num))

if __name__ == '__main__':
    main()