import pandas as pd
import yfinance as yf
import ta

def get_data():
    ticker = "^BSESN"  # Sensex ticker
    df = yf.download(ticker, interval="5m", period="1d", progress=False)

    if df.empty or 'Close' not in df.columns:
        raise ValueError("No data fetched. Market might be closed or ticker invalid.")

    df = df[['Open', 'High', 'Low', 'Close', 'Volume']].dropna()

    # Indicators
    df['EMA20'] = ta.trend.EMAIndicator(close=df['Close'], window=20).ema_indicator()
    df['RSI'] = ta.momentum.RSIIndicator(close=df['Close'], window=14).rsi()
    macd = ta.trend.MACD(close=df['Close'])
    df['MACD'] = macd.macd()
    df['MACD_signal'] = macd.macd_signal()
    df['ATR'] = ta.volatility.AverageTrueRange(high=df['High'], low=df['Low'], close=df['Close'], window=14).average_true_range()

    df.dropna(inplace=True)
    return df

def generate_signal(df):
    latest = df.iloc[-1]

    ema = latest['EMA20']
    rsi = latest['RSI']
    macd = latest['MACD']
    macd_signal = latest['MACD_signal']
    close = latest['Close']
    atr = latest['ATR']

    # Signal logic
    signal = "Hold"
    reason = ""

    if macd > macd_signal and close > ema and rsi > 55:
        signal = "Buy Call"
        reason = "MACD crossover + EMA support + RSI strength"
    elif macd < macd_signal and close < ema and rsi < 45:
        signal = "Buy Put"
        reason = "MACD bearish crossover + below EMA + weak RSI"
    elif macd > macd_signal and rsi < 50:
        signal = "Sell Put"
        reason = "MACD bullish + RSI rising"
    elif macd < macd_signal and rsi > 50:
        signal = "Sell Call"
        reason = "MACD bearish + RSI falling"

    # ATR filter: avoid trading in low volatility
    if atr < (df['ATR'].mean() * 0.5):
        signal = "Hold"
        reason = "Low volatility (ATR filter)"

    return signal, reason
