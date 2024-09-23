def main():
    height, width = [int(input()) for _ in range(1, 3)]
    spaces = 0
    for i in range(height):
        number = i + 1
        for j in range(width):
            if spaces != width:
                print(f'{number:>{len(str(height * width))}}', end=' ')
            else:
                print(f'\n{number:>{len(str(height * width))}}', end=' ')
                spaces = 0
            spaces += 1
            number += height


if __name__ == "__main__":
    main()
