import yfinance as yf
import ta
import pandas as pd

def get_data():
    df = yf.download("^BSESN", interval="15m", period="60d", progress=False)

    if df.empty or 'Close' not in df.columns:
        raise ValueError("Failed to fetch Sensex data or 'Close' column missing.")

    df['EMA20'] = ta.trend.EMAIndicator(close=df['Close'], window=20).ema_indicator()
    df['RSI'] = ta.momentum.RSIIndicator(close=df['Close'], window=14).rsi()
    
    df.dropna(inplace=True)
    
    return df

def generate_signal(df):
    latest = df.iloc[-1]
    if latest['RSI'] < 30 and latest['Close'] > latest['EMA20']:
        return "📈 BUY CALL (Uptrend)", latest
    elif latest['RSI'] > 70 and latest['Close'] < latest['EMA20']:
        return "📉 BUY PUT (Downtrend)", latest
    else:
        return "⏸️ HOLD (No strong signal)", latest
