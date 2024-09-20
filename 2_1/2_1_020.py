def main():
    N = int(input())
    M = int(input())
    K1 = int(input())
    K2 = int(input())

    answer = []
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i + j == N and i * K1 + j * K2 == M * N:
                answer.append([i, j])

    print(answer[0][0], answer[0][1])

if __name__ == '__main__':
    main()