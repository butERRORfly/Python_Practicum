import pandas as pd
import re


def length_stats(text):
    words = re.findall(r"[a-zа-яё']+", text.lower())
    word_lengths = {word: len(word) for word in words}
    series = pd.Series(word_lengths).sort_index()

    return series