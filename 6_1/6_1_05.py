import math


def main():
    x1, y1 = map(float, input().split())
    rho, phi = map(float, input().split())

    x2 = rho * math.cos(phi)
    y2 = rho * math.sin(phi)

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(distance)


if __name__ == '__main__':
    main()
