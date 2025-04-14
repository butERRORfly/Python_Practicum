def get_long(series, min_length=5):
    return series[series.index.str.len() >= min_length]