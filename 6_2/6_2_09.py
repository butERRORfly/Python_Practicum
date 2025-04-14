import pandas as pd
import sys


def main():
    first_line = sys.stdin.readline()
    second_line = sys.stdin.readline()

    x1, y1 = map(int, first_line.strip().split())
    x2, y2 = map(int, second_line.strip().split())

    x_min = min(x1, x2)
    x_max = max(x1, x2)
    y_min = min(y1, y2)
    y_max = max(y1, y2)

    data = pd.read_csv('data.csv')

    filtered = data[
        (data['x'] >= x_min) &
        (data['x'] <= x_max) &
        (data['y'] >= y_min) &
        (data['y'] <= y_max)
    ]

    print(filtered.to_string())


if __name__ == "__main__":
    main()
