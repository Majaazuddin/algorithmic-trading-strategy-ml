"""
Handles loading and cleaning of historical stock data.
"""

import pandas as pd

def load_data(file_path):
    """
    Loads and cleans stock price data
    """
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()

    numeric_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

    df.dropna(inplace=True)
    return df
