import yfinance as yf
import pandas as pd
import ta

def get_data():
    ticker = "^BSESN"
    df = yf.download(ticker, interval="5m", period="1d")
    df.dropna(inplace=True)
    df = df[['Close']]
    df['EMA20'] = ta.trend.EMAIndicator(close=df['Close'], window=20).ema_indicator()
    df['RSI'] = ta.momentum.RSIIndicator(close=df['Close'], window=14).rsi()
    macd = ta.trend.MACD(close=df['Close'])
    df['MACD'] = macd.macd()
    df['MACD_signal'] = macd.macd_signal()
    df['MACD_hist'] = macd.macd_diff()

    df.dropna(inplace=True)
    df['Signal'] = df.apply(lambda row: determine_signal(row), axis=1)
    return df

def determine_signal(row):
    rsi = row['RSI']
    close = row['Close']
    ema = row['EMA20']
    macd = row['MACD']
    macd_signal = row['MACD_signal']

    if rsi < 30 and close > ema and macd > macd_signal:
        return "Buy Call"
    elif rsi > 70 and close < ema and macd < macd_signal:
        return "Sell Call"
    elif rsi > 70 and close > ema and macd < macd_signal:
        return "Buy Put"
    elif rsi < 30 and close < ema and macd > macd_signal:
        return "Sell Put"
    else:
        return "Hold"

def generate_latest_signal(df):
    latest_row = df.iloc[-1]
    return latest_row['Signal'], latest_row
