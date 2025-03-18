import math


def main(x) -> float:
    log32_x = math.log(x) / math.log(32)
    first_term = (3 / 16) * log32_x

    angle = (math.pi * x) / (2 * math.e)
    cos_value = math.cos(angle)
    second_term = math.pow(x, cos_value)

    sin_value = math.sin(x / math.pi)
    third_term = math.pow(sin_value, 2)

    result = first_term + second_term - third_term
    return result


if __name__ == "__main__":
    x = float(input())
    print(main(x))
