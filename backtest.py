def backtest(df):
    results = []
    for i in range(20, len(df)):
        row = df.iloc[i]
        prev = df.iloc[i - 1]

        if row['RSI'] < 30 and row['Close'] > row['EMA20']:
            results.append(("BUY CALL", row.name, row['Close']))
        elif row['RSI'] > 70 and row['Close'] < row['EMA20']:
            results.append(("BUY PUT", row.name, row['Close']))

    return results
