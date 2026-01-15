# 📈 Algorithmic Trading Strategy with Machine Learning

## 📌 Project Overview
This project is an end-to-end **Algorithmic Trading System** built using Python.  
It analyzes historical stock price data, generates trading signals using **technical indicators and machine learning**, backtests multiple strategies, and compares their performance using professional metrics and visualizations.

The goal of this project is to demonstrate:
- How trading strategies are built step-by-step
- How machine learning can be integrated into trading systems
- How to evaluate and compare strategies like a real quant or data scientist

---

## 🧠 Strategies Implemented

### 1️⃣ Buy & Hold (Benchmark)
- Always invested in the stock
- Used as a baseline to compare other strategies
- Represents a passive investing approach

---

### 2️⃣ SMA Crossover Strategy
- Uses **Simple Moving Averages (SMA 20 & SMA 50)**
- **Buy Signal:** SMA 20 crosses above SMA 50 (Golden Cross)
- **Sell Signal:** SMA 20 crosses below SMA 50 (Death Cross)
- A classic rule-based trading strategy

---

### 3️⃣ Machine Learning Strategy
- Uses **Logistic Regression**
- Features used:
  - `SMA_20`
  - `SMA_50`
- The model predicts whether the price will go **up or down**
- Trades are executed based on model predictions
- Signals are shifted to avoid **look-ahead bias**

---

## 📊 Performance Metrics
Each strategy is evaluated using:

- **Total Return (%)**
- **Maximum Drawdown (%)**
- **Sharpe Ratio**
- **Equity Curve Visualization**

This allows a fair comparison between:
- Buy & Hold
- SMA Strategy
- Machine Learning Strategy

---
## 📁 Project Structure

Algorithmic-Trading-Strategy/
│
├── data/
│ ├── AAPL_stock_data.csv
│ └── AAPL_stock_data_cleaned.csv
│
├── src/
│ ├── data_loader.py # Loads and cleans data
│ ├── indicators.py # Technical indicators (SMA)
│ ├── strategies.py # Buy & Hold and SMA strategies
│ ├── ml_model.py # Machine Learning model training
│ ├── backtester.py # Backtesting engine
│
├── main.py # Main execution file
├── README.md # Project documentation
## 📁 Project Structure

