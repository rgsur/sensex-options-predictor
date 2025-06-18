import backtrader as bt

class MACDStrategy(bt.Strategy):
    def __init__(self):
        self.macd = bt.indicators.MACD()
        self.cross = bt.indicators.CrossOver(self.macd.macd, self.macd.signal)

    def next(self):
        if self.cross > 0:
            self.buy()
        elif self.cross < 0:
            self.sell()
