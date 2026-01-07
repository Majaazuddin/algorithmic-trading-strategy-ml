import numpy as np
import pandas as pd


def backtest_strategy(df, signal_column, initial_capital=10000):
    """
    Generic backtesting function.
    Buys when signal == 1, stays in cash when signal == 0.
    """

    df = df.copy()

    # Daily returns
    df['Market_Return'] = df['Close'].pct_change()

    # Strategy returns
    df['Strategy_Return'] = df['Market_Return'] * df[signal_column].shift(1)

    # Replace NaN with 0
    df['Strategy_Return'] = df['Strategy_Return'].fillna(0)

    # Equity curve
    df['Equity'] = (1 + df['Strategy_Return']).cumprod() * initial_capital

    return df
