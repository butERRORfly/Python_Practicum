import numpy as np


def rotate(matrix, angle):
    arr = np.array(matrix)

    angle = angle % 360

    if angle == 90:
        return np.rot90(arr, k=-1)
    elif angle == 180:
        return np.rot90(arr, k=2)
    elif angle == 270:
        return np.rot90(arr, k=1)
    else:
        return arr.copy()
