def main():
    height, width = [int(input()) for _ in range(1, 3)]
    spaces = 0
    for i in range(1, height * width + 1):
        if spaces != width:
            print(f'{i:>{len(str(height * width))}}', end=' ')
        else:
            print(f'\n{i:>{len(str(height * width))}}', end=' ')
            spaces = 0
        spaces += 1


if __name__ == "__main__":
    main()
