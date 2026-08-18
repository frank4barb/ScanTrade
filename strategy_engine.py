"""
ScanTrade - Strategy Engine
Definizione delle regole operative e Risk Management.
"""

from data_engine import DataEngine

class StrategyEngine:
    def __init__(self, fast_window=20, slow_window=50, rsi_sell=70, stop_loss_pct=0.03, take_profit_pct=0.08):
        self.fast_window = fast_window
        self.slow_window = slow_window
        self.rsi_sell = rsi_sell
        self.stop_loss_pct = stop_loss_pct
        self.take_profit_pct = take_profit_pct

    def generate_signals(self, df):
        data = DataEngine.add_indicators(
            df,
            fast_sma=self.fast_window,
            slow_sma=self.slow_window
        ).copy()
        
        data['Signal'] = 0
        trend_bull = data['SMA_Fast'] > data['SMA_Slow']
        trend_bear = data['SMA_Fast'] < data['SMA_Slow']
        
        buy_condition = trend_bull & (data['RSI'] > 45) & (data['RSI'] < self.rsi_sell)
        sell_condition = trend_bear | (data['RSI'] > self.rsi_sell)
        
        data.loc[buy_condition, 'Signal'] = 1
        data.loc[sell_condition, 'Signal'] = -1
        return data