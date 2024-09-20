def main():
    stroke1 = input()
    stroke2 = input()
    stroke3 = input()

    dic = {}

    for i in [stroke1, stroke2, stroke3]:
        if 'зайка' in i:
            dic[i] = dic.get(i, 0) + len(i)

    mini_stroke = 9999 * 'р'
    for i in dic.keys():
        mini_stroke = min(mini_stroke, i)

    print(f'{mini_stroke} {len(mini_stroke)}')


if __name__ == '__main__':
    main()