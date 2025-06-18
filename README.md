# 📈 Sensex Options Price Movement Predictor (5‑Minute Timeframe)

A real-time trading strategy tool for Sensex options using **EMA20**, **RSI14**, and **MACD** indicators to generate precise **Buy Call, Sell Call, Buy Put, Sell Put** entry and exit signals. Built with **Streamlit**, **yfinance**, and **Plotly**.

---

## ✅ Features

- 📊 Fetches live **5-minute** interval data from Yahoo Finance
- 📈 Calculates **EMA20**, **RSI14**, **MACD**, and **MACD signal line**
- 🎯 Generates exact signals:
  - **Buy Call**  – RSI < 30, Price > EMA20, MACD > Signal
  - **Sell Call** – RSI > 70, Price < EMA20, MACD < Signal
  - **Buy Put**   – RSI > 70, Price > EMA20, MACD < Signal
  - **Sell Put**  – RSI < 30, Price < EMA20, MACD > Signal
- 📌 Displays the current signal in color-coded form
- 📉 Shows the last 10 signals in an interactive table
- 📈 Plots price and EMA20 with markers for each signal type  
- ⏳ Auto-refreshes every 5 minutes with countdown timer + manual refresh button

---

## 🛠️ Tech Stack

- Python 3.x  
- [Streamlit](https://streamlit.io/)  
- [Pandas](https://pandas.pydata.org/)  
- [yfinance](https://github.com/ranaroussi/yfinance)  
- [TA Lib (`ta`)](https://technical-analysis-library-in-python.readthedocs.io/)  
- [Plotly](https://plotly.com/python/)  

---

## 🚀 Quick Start — Local

```bash
git clone https://github.com/rgsur/sensex-options-predictor.git
cd sensex-options-predictor
pip install -r requirements.txt
streamlit run app.py
