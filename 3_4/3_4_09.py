def main():
    num = int(input())
    for i in [[(i + 1) * (j + 1) for j in range(num)] for i in range(num)]:
        print(*i)


if __name__ == "__main__":
    main()
