def main():

    dic = {}

    while stroke := input():
        list_stroke = list(map(str, stroke.split()))
        breaker = None
        for item in list_stroke:
            if breaker == 'зайка':
                dic[item] = dic.get(item, 0) + 1
            if item == 'зайка':
                if breaker:
                    dic[breaker] = dic.get(breaker, 0) + 1
            breaker = item

    for i in dic:
        print(i)


if __name__ == '__main__':
    main()
