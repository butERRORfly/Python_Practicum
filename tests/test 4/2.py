import numpy as np


def update_cols(array, size, value, *cols):
    new_array = array.copy()
    reshaped_array = new_array.reshape(size)
    unique_cols = sorted(set(cols))
    for col in unique_cols:
        if col < reshaped_array.shape[1]:
            reshaped_array[:, col] += value
    return new_array