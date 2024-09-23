def main():
    height, width = [int(input()) for _ in range(1, 3)]
    det = [[0] * width for _ in range(height)]
    for i in range(height):
        for j in range(width):
            row = i + 1
            val = j + 1
            det[i][j] = f'{((row - 1) * width + val):>{len(str(height * width))}}'

    for i in range(height):
        if i % 2 != 0:
            det[i] = det[i][::-1]
        print(*det[i])

if __name__ == "__main__":
    main()
