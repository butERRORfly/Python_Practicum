def main():
    with open(input(), 'r') as f:
        lines = f.readlines()

    border = int(input())
    for i in lines[-border::]:
        print(i[:-1:])


if __name__ == '__main__':
    main()
