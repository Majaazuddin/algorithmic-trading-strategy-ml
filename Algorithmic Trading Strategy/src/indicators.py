"""
Contains technical indicator calculations.
"""

def add_sma(df, short_window=20, long_window=50):
    """
    Adds Simple Moving Averages to the dataframe.

    Parameters:
    df : pandas DataFrame
        Must contain a 'Close' column
    """
    df['SMA_20'] = df['Close'].rolling(window=short_window).mean()
    df['SMA_50'] = df['Close'].rolling(window=long_window).mean()
    return df
