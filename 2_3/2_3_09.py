def main():
    num = int(input())

    answer = 1
    for i in range(1, num + 1):
        answer = answer * i
    print(answer)

if __name__ == '__main__':
    main()