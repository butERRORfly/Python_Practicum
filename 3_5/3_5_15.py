from sys import stdin
import json


def main():
    with open('scoring.json', 'r') as f:
        records = json.load(f)

    answers = []
    for i in stdin:
        answers.append(i.strip('\n'))

    total = 0
    for i in records:
        index = int(i['points']) // len(i['tests'])
        for test in i['tests']:
            good_answer = test['pattern']
            for answer in answers:
                if answer == good_answer:
                    total += index

    print(total)


if __name__ == '__main__':
    main()
