import json
from sys import stdin


def main():
    file = input()
    with open(file, encoding="UTF-8") as f:
        records = json.load(f)

    for line in stdin:
        if line:
            line = line.split('==')
            records[line[0].strip()] = line[1].strip()

    with open(file, 'w', encoding='UTF-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()
