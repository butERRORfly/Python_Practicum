def main():
    v1 = int(input())
    v2 = int(input())
    v3 = int(input())

    dic_speed = {"Петя": v1, "Вася": v2, "Толя": v3}
    dic_speed = sorted(dic_speed.items(), key=lambda x: x[1], reverse=True)

    for val, id in enumerate(dic_speed):
        print(f'{val + 1}. {id[0]}')

if __name__ == '__main__':
    main()