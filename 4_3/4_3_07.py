def same_type(oldFunc):
    tmp = []

    def newFunc(*args):
        typeTmp = type(args[0])
        tmp.append(typeTmp)
        if all(type(x) is typeTmp for x in args[1::]):
            return oldFunc(*args)

        print('Обнаружены различные типы данных')

    return newFunc
