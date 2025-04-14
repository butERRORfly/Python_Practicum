import pandas as pd
import numpy as np
import re


def length_stats(text):
    words = re.findall(r"[a-zа-яё']+", text.lower())
    word_lengths_odd = {word: len(word) for word in words if len(word) % 2 != 0}
    series_odd = pd.Series(word_lengths_odd, dtype=np.int64).sort_index()

    word_lengths_even = {word: len(word) for word in words if len(word) % 2 == 0}
    series_even = pd.Series(word_lengths_even, dtype=np.int64).sort_index()

    return series_odd, series_even
