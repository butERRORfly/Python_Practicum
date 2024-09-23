def main():
    height, width = [int(input()) for _ in range(1, 3)]
    det = [[0] * width for _ in range(height)]
    for i in range(height):
        row = i + 1
        for j in range(width):
            val = j + 1
            det[i][j] = f'{row:>{len(str(height * width))}}'
            row += height

    a = []
    for j in range(width):
        a.append([x[j] for x in det][::-1])

    for i in range(height):
        for j in range(width):
            if j % 2 != 0:
                det[i][j] = a[j][i]

    for i in range(height):
        print(*det[i])

if __name__ == "__main__":
    main()
