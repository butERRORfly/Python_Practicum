def main():
    num = int(input())
    print(sum(int(x) for x in str(num)))

if __name__ == '__main__':
    main()