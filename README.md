# 📈 Algorithmic Trading Strategy with Machine Learning

## 📌 Overview
This project is an end-to-end **algorithmic trading system** built in Python.  
It analyzes historical stock data, generates trading signals using **technical indicators and machine learning**, backtests multiple strategies, and compares their performance using **equity curves**.

The project progresses from **simple rule-based strategies** to a **machine-learning-driven strategy**, following best practices used in real-world quantitative trading systems.

---

## 🧠 Strategies Implemented

### 1️⃣ Buy & Hold (Benchmark)
- Always invested in the stock
- Used as a baseline for comparison

### 2️⃣ SMA Crossover Strategy
- Uses **Simple Moving Averages (SMA 20 & SMA 50)**
- **Buy** when SMA 20 > SMA 50  
- **Exit** when SMA 20 < SMA 50

### 3️⃣ Machine Learning Strategy
- Logistic Regression model
- Features: `SMA_20`, `SMA_50`
- Predicts whether the price will move up
- Trades based on model predictions
- Signal is shifted to avoid **look-ahead bias**

---

## 
 Project Structure
