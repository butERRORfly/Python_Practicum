import json


def main():
    file1, file2 = [input() for _ in range(2)]

    with open(file1, 'r') as f:
        lines = f.readlines()

        data = []
        for i in lines:
            data += list(map(int, i.split()))

    average = f'{(sum(data) / len(data)):.2f}'
    records = {
        "count": len(data),
        "positive_count": len([x for x in data if x > 0]),
        "min": min(data),
        "max": max(data),
        "sum": sum(data),
        "average": float(average),
    }

    with open(file2, 'w', encoding='UTF-8') as file:
        json.dump(records, file, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()
