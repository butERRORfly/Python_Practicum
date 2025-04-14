import pandas as pd
import numpy as np


def values(func, start, end, step):
    x_values = np.arange(start, end + step, step)
    y_values = [func(x) for x in x_values]
    return pd.Series(y_values, index=x_values, dtype='float64')


def min_extremum(data):
    return data.idxmin()


def max_extremum(data):
    return data.idxmax()
