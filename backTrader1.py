import pandas as pd
import backtrader as bt
import matplotlib.pyplot as plt

class MyStrategy (bt.Strategy):
    def next (self):
        pass # Do something

cerebro = bt.Cerebro()

cerebro.addstrategy(MyStrategy)

cerebro.run()