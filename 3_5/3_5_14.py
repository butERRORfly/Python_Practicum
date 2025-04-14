import json


def main():
    file1, file2 = [input() for _ in range(2)]

    with open(file1, 'r') as file_in:
        users = json.load(file_in)

    with open(file2, 'r') as file_in:
        updates = json.load(file_in)

    names = {}
    for i in users:
        name = i.pop('name')
        names[name] = i

    for i in updates:
        name = i.pop('name')
        if name not in names:
            names[name] = {}
        for j in i:
            if names[name].get(j, '') < i[j]:
                names[name][j] = i[j]

    with open(file1, 'w') as f:
        json.dump(names, f, ensure_ascii=False, indent=4, sort_keys=False)


if __name__ == '__main__':
    main()
