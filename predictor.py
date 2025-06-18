import yfinance as yf
import pandas as pd
import ta

def get_data():
    symbol = "^BSESN"
    df = yf.download(tickers=symbol, interval='5m', period='5d')

    if df.empty or 'Close' not in df.columns:
        raise ValueError("Downloaded data is empty or missing 'Close' column.")

    # ✅ Make sure 'Close' is a Series, not a 2D array
    close_series = pd.Series(df['Close'].values.flatten(), index=df.index)

    # Calculate indicators
    df['EMA20'] = ta.trend.EMAIndicator(close=close_series, window=20).ema_indicator()
    df['RSI'] = ta.momentum.RSIIndicator(close=close_series, window=14).rsi()

    df.dropna(inplace=True)
    return df

def generate_signal(df):
    # Use only the latest values (last row)
    rsi = df['RSI'].iloc[-1]
    close = df['Close'].iloc[-1]
    ema20 = df['EMA20'].iloc[-1]

    if rsi < 30 and close > ema20:
        signal = "Buy Call"
    elif rsi > 70 and close < ema20:
        signal = "Sell Call"
    elif rsi < 30 and close < ema20:
        signal = "Buy Put"
    elif rsi > 70 and close > ema20:
        signal = "Sell Put"
    else:
        signal = "Hold"

    df['Signal'] = "Hold"
    df.at[df.index[-1], 'Signal'] = signal

    return signal, df
