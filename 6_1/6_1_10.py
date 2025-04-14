import numpy as np


def stairs(vector):
    v = np.array(vector)
    n = len(v)
    indices = np.arange(n)
    offset_indices = (-indices[:, None] + indices) % n
    return v[offset_indices]
