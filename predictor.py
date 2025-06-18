import yfinance as yf
import pandas as pd
import ta

def get_data():
    # Download Sensex data - 1 hour interval for last 30 days
    df = yf.download("^BSESN", interval="1h", period="30d", progress=False)

    if df.empty or 'Close' not in df.columns:
        raise ValueError("Data fetch failed or 'Close' column missing")

    # Ensure 'Close' is a 1D Series
    close_series = df['Close'].squeeze()

    # Technical indicators
    ema20 = ta.trend.EMAIndicator(close=close_series, window=20).ema_indicator()
    rsi14 = ta.momentum.RSIIndicator(close=close_series, window=14).rsi()

    # Add indicators to the DataFrame
    df['EMA20'] = ema20
    df['RSI'] = rsi14

    # Drop rows with NaN values (caused by indicator warm-up period)
    df.dropna(inplace=True)

    return df

def generate_signal(df):
    """
    Signal strategy:
    - BUY: Close > EMA20 and RSI < 70
    - SELL: Close < EMA20 and RSI > 30
    - HOLD: Otherwise
    """
    # Make sure we're working with the last row
    latest = df.iloc[-1]

    # Extract actual values (scalars) from the latest row
    close = float(latest['Close'])
    ema20 = float(latest['EMA20'])
    rsi = float(latest['RSI'])

    if close > ema20 and rsi < 70:
        signal = "BUY"
    elif close < ema20 and rsi > 30:
        signal = "SELL"
    else:
        signal = "HOLD"

    return signal, latest

