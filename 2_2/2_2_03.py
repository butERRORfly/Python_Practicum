def main():
    v1 = int(input())
    v2 = int(input())
    v3 = int(input())
    if max(v1, v2, v3) == v1:
        print('Петя')
    if max(v1, v2, v3) == v2:
        print('Вася')
    if max(v1, v2, v3) == v3:
        print('Толя')

if __name__ == '__main__':
    main()