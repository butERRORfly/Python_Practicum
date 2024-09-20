def main():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    row1 = [str(num1)[0], str(num2)[0], str(num3)[0]]
    row2 = [str(num1)[1], str(num2)[1], str(num3)[1]]

    if len(set(row1)) == 1:
        print(row1[0])
    else:
        print(row2[0])

if __name__ == '__main__':
    main()