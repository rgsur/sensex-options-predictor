import yfinance as yf
import pandas as pd
import ta

def get_data():
    # Download 5-minute intraday Sensex data for today
    df = yf.download("^BSESN", interval="5m", period="1d", progress=False)

    if df.empty:
        raise ValueError("No data fetched. Check your connection or ticker.")

    # Reset index and keep only needed columns
    df = df.reset_index()[['Datetime', 'Close']].copy()

    # Ensure Close is a proper 1D numeric Series
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    df = df.dropna()

    # Extract Series for indicators
    close_series = pd.Series(df['Close'].values, index=df.index)

    # EMA20
    ema_indicator = ta.trend.EMAIndicator(close=close_series, window=20)
    df['EMA20'] = ema_indicator.ema_indicator()

    # RSI
    rsi_indicator = ta.momentum.RSIIndicator(close=close_series, window=14)
    df['RSI'] = rsi_indicator.rsi()

    # MACD
    macd_indicator = ta.trend.MACD(close=close_series)
    df['MACD'] = macd_indicator.macd()
    df['MACD_Signal'] = macd_indicator.macd_signal()

    # Drop rows with NaN (from indicator warm-up period)
    df = df.dropna()

    return df


def generate_signal(df):
    latest = df.iloc[-1]

    close = latest['Close']
    ema = latest['EMA20']
    rsi = latest['RSI']
    macd = latest['MACD']
    macd_signal = latest['MACD_Signal']

    # Strategy
    if close > ema and rsi > 60 and macd > macd_signal:
        return "Buy Call"
    elif close < ema and rsi < 40 and macd < macd_signal:
        return "Buy Put"
    elif close > ema and macd < macd_signal:
        return "Sell Call"
    elif close < ema and macd > macd_signal:
        return "Sell Put"
    else:
        return "Hold"
