import numpy as np


def multiplication_matrix(n):
    return np.array([[(i + 1) * (j + 1) for j in range(n)] for i in range(n)])
