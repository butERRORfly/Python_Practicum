N = int(input())
M = int(input())

print('; '.join([str(i) for i in range(N, M - 1, -((N - M) // 3))]))
print('Старт!')