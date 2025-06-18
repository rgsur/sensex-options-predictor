# 📈 Sensex Options Price Movement Predictor

A real-time prediction app using technical indicators (EMA and RSI) to generate actionable option trading signals:

- **BUY CALL**
- **SELL CALL**
- **BUY PUT**
- **SELL PUT**

## 🔧 Tech Stack

- Python
- Pandas
- TA-Lib (`ta` package)
- Yahoo Finance (`yfinance`)
- Streamlit

## 📉 Strategy

| Indicator | Rule |
|----------|------|
| RSI < 30 & Price > EMA20 | BUY CALL |
| RSI > 70 & Price < EMA20 | SELL CALL |
| RSI > 70 & Price > EMA20 | SELL PUT |
| RSI < 30 & Price < EMA20 | BUY PUT |

## 🚀 How to Run

### 1. Clone and Setup
```bash
git clone https://github.com/YOUR_USERNAME/sensex-options-predictor.git
cd sensex-options-predictor
pip install -r requirements.txt
