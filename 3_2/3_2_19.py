def main():
    _dict = {}
    for i in range(int(input())):
        name = input().split(': ')
        for j in name[1::]:
            _dict[name[0]] = _dict.get(name[0], set()) | set([x for x in j.split(', ')])

    answer = {y: 0 for x in _dict.values() for y in x}
    for i in _dict.keys():
        for j in _dict[i]:
            answer[j] = answer.get(j, 0) + 1

    print('\n'.join(sorted([x for x in answer.keys() if answer[x] == 1])))


if __name__ == '__main__':
    main()
