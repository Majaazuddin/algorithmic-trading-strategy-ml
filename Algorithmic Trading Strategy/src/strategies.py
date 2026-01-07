"""
Defines trading strategies and their return calculations.
"""

import pandas as pd


def buy_and_hold(df):
    """
    Buy & Hold strategy:
    Always stay invested in the market.
    """
    df['BH_Return'] = df['Close'].pct_change()
    df['BH_Return'] = df['BH_Return'].fillna(0)
    return df


def sma_strategy(df):
    """
    Simple Moving Average crossover strategy.
    Buy when SMA_20 > SMA_50.
    """
    df['SMA_Signal'] = (df['SMA_20'] > df['SMA_50']).astype(int)
    df['SMA_Return'] = df['SMA_Signal'].shift(1) * df['Close'].pct_change()
    df['SMA_Return'] = df['SMA_Return'].fillna(0)
    return df
