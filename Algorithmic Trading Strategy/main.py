"""
Main execution file for the Algorithmic Trading Strategy project.

Steps:
1. Load historical stock data
2. Add technical indicators
3. Apply Buy & Hold, SMA, and ML strategies
4. Backtest each strategy
5. Plot equity curve comparison
"""

import matplotlib.pyplot as plt

from src.data_loader import load_data
from src.indicators import add_sma
from src.strategies import sma_strategy
from src.ml_model import train_ml_model
from src.backtester import backtest_strategy

# ===============================
# 1️⃣ LOAD DATA
# ===============================
df = load_data("data/AAPL_stock_data_cleaned.csv")

# ===============================
# 2️⃣ ADD INDICATORS
# ===============================
df = add_sma(df)

# ===============================
# 3️⃣ BUY & HOLD SIGNAL
# ===============================
# Buy & Hold = always invested
df['BH_Signal'] = 1

# ===============================
# 4️⃣ SMA STRATEGY SIGNAL
# ===============================
df = sma_strategy(df)   # creates SMA_Signal

# ===============================
# 5️⃣ MACHINE LEARNING STRATEGY
# ===============================
model, df = train_ml_model(df)

# ML predictions → signal
df['ML_Signal'] = model.predict(df[['SMA_20', 'SMA_50']])

# Shift to avoid look-ahead bias
df['ML_Signal'] = df['ML_Signal'].shift(1).fillna(0)

# ===============================
# 6️⃣ BACKTEST ALL STRATEGIES
# ===============================

# Buy & Hold
bh_df = backtest_strategy(df, signal_column='BH_Signal')
df['BH_Equity'] = bh_df['Equity']

# SMA Strategy
sma_df = backtest_strategy(df, signal_column='SMA_Signal')
df['SMA_Equity'] = sma_df['Equity']

# ML Strategy
ml_df = backtest_strategy(df, signal_column='ML_Signal')
df['ML_Equity'] = ml_df['Equity']

# ===============================
# 7️⃣ PLOT EQUITY CURVES
# ===============================
plt.figure(figsize=(12, 6))
plt.plot(df['BH_Equity'], label='Buy & Hold')
plt.plot(df['SMA_Equity'], label='SMA Strategy')
plt.plot(df['ML_Equity'], label='ML Strategy')

plt.title("Equity Curve Comparison")
plt.xlabel("Date")
plt.ylabel("Portfolio Value")
plt.legend()
plt.grid(True)
plt.show()
