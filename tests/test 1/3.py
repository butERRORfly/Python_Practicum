# N = int(input())
# M = int(input())
# print('; '.join([str(i) for i in range(N, M - 1, -((N - M) // 3))]))
# print('Старт!')


def main():
    N, M = [int(input()) for _ in range(2)]
    print('; '.join([str(i) for i in range(N, M - 1, -((N - M) // 3))]), '\nСтарт!')


if __name__ == '__main__':
    main()