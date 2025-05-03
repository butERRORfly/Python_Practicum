import math
import sys


def compute_f(x):
    numerator = math.sin(math.pi - x) * math.cos(math.pi / 2 + x) * math.tan(x - math.pi / 2)
    denominator = math.cos(math.pi / 2 - x) * math.cos(math.pi / 2 - x) * math.tan(x - math.pi)
    return numerator / denominator


if __name__ == '__main__':
    for line in sys.stdin:
        x = float(line.strip())
        try:
            result = compute_f(x)
            print(f"{result:.3f}")
        except ZeroDivisionError:
            print("ZeroDivisionError")