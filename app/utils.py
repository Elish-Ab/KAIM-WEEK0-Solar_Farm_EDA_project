import pandas as pd
from scipy.stats import zscore

def detect_anomalies(data, columns=['GHI', 'DNI', 'DHI', 'Tamb', 'WS', 'WSgust']):
    z_scores = data[columns].apply(zscore)
    outliers = (z_scores.abs() > 3).any(axis=1)
    return data[outliers]

def clean_data(data, columns=['GHI', 'DNI', 'DHI', 'Tamb', 'WS', 'WSgust']):
    z_scores = data[columns].apply(zscore)
    outliers = (z_scores.abs() > 3).any(axis=1)
    return data[~outliers]
