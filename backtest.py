def backtest(df):
    results = []

    for i, row in df.iterrows():
        rsi = float(row['RSI'])
        close = float(row['Close'])
        ema20 = float(row['EMA20'])

        if rsi < 30 and close > ema20:
            signal = 'BUY'
        elif rsi > 70 and close < ema20:
            signal = 'SELL'
        else:
            signal = 'HOLD'

        # Use the index `i` as timestamp
        results.append((signal, i, close))

    return results
