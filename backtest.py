def backtest(df):
    signals = []
    position = None
    results = []

    for i, row in df.iterrows():
        rsi = float(row['RSI'])
        close = float(row['Close'])
        ema20 = float(row['EMA20'])

        if rsi < 30 and close > ema20:
            signal = 'BUY CALL'
        elif rsi > 70 and close < ema20:
            signal = 'SELL CALL'
        elif rsi > 70 and close > ema20:
            signal = 'SELL PUT'
        elif rsi < 30 and close < ema20:
            signal = 'BUY PUT'
        else:
            signal = 'HOLD'

        signals.append(signal)
        results.append((signal, i, close))

    df['Signal'] = signals
    return results
