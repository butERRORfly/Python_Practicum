def main():
    start, stop, step = list(map(float, input().split()))

    while float(f'{start:.2f}') <= float(f'{stop:.2f}'):
        print(f'{start:.2f}')
        start += step


if __name__ == "__main__":
    main()
