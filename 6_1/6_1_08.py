import numpy as np


def snake(M, N, direction='H'):
    arr = np.arange(1, M * N + 1, dtype=np.int16)

    if direction == 'H':
        arr = arr.reshape(N, M)
        for i in range(1, N, 2):
            arr[i] = arr[i, ::-1]
    elif direction == 'V':
        arr = arr.reshape(M, N).T
        for j in range(1, M, 2):
            arr[:, j] = arr[::-1, j]

    return arr
