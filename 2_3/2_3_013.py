def main():
    count = int(input())
    mini = 9999 * 'р'
    for i in range(count):
        name = input()
        if name < mini:
            mini = name
    print(mini)

if __name__ == '__main__':
    main()