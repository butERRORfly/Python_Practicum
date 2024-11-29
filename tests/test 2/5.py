from sys import stdin
import json


def main():
    data = []
    for line in stdin:
        data.append(int(line.strip('\n')))

    def setKeys(num):
        return sorted(set([int(x) for x in str(num)]))

    globalListKeys = []
    for i in data:
        globalListKeys.extend(setKeys(i))

    records = {}
    for i in sorted(set(globalListKeys)):
        records[i] = records.get(i, []) + []

    for key in records:
        for i in data:
            if str(key) in str(i):
                records[key] = records.get(key, []) + [i]

    for key in list(records.keys()):
        records[key] = sorted(list(set(records[key])))
        if records[key] in (None, [], '', {}):
            del records[key]

    with open('result.json', 'w') as f:
        json.dump(records, f, indent=4, ensure_ascii=False, sort_keys=True)


if __name__ == '__main__':
    main()
