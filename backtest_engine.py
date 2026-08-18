"""
ScanTrade - Backtest Engine
Simulazione della gestione portafoglio, posizioni e costi.
"""

import pandas as pd

class BacktestEngine:
    def __init__(self, initial_capital=10000.0, commission_pct=0.001, slippage_pct=0.0005):
        self.initial_capital = initial_capital
        self.commission_pct = commission_pct
        self.slippage_pct = slippage_pct

    def run(self, df, strategy):
        data = strategy.generate_signals(df)
        capital = float(self.initial_capital)
        position = 0.0
        entry_price = 0.0
        entry_date = None
        
        equity_curve = []
        trades = []
        
        for i in range(len(data)):
            date = data.index[i]
            close = float(data['Close'].iloc[i])
            high = float(data['High'].iloc[i])
            low = float(data['Low'].iloc[i])
            signal = int(data['Signal'].iloc[i])
            
            # Controllo posizioni aperte (Stop Loss / Take Profit / Exit Signal)
            if position > 0:
                sl_price = entry_price * (1 - strategy.stop_loss_pct)
                tp_price = entry_price * (1 + strategy.take_profit_pct)
                
                exit_price = None
                exit_reason = None
                
                if low <= sl_price:
                    exit_price = sl_price * (1 - self.slippage_pct)
                    exit_reason = "Stop Loss"
                elif high >= tp_price:
                    exit_price = tp_price * (1 - self.slippage_pct)
                    exit_reason = "Take Profit"
                elif signal == -1:
                    exit_price = close * (1 - self.slippage_pct)
                    exit_reason = "Signal Exit"
                    
                if exit_price is not None:
                    proceeds = position * exit_price
                    commission = proceeds * self.commission_pct
                    capital = proceeds - commission
                    pnl = (exit_price - entry_price) / entry_price
                    trades.append({
                        'Entry Date': entry_date,
                        'Exit Date': date,
                        'Entry Price': entry_price,
                        'Exit Price': exit_price,
                        'PnL (%)': pnl * 100,
                        'Reason': exit_reason
                    })
                    position = 0.0
                    entry_price = 0.0
                    entry_date = None

            # Controllo ingresso in posizione
            if position == 0 and signal == 1:
                buy_price = close * (1 + self.slippage_pct)
                commission = capital * self.commission_pct
                investable = capital - commission
                position = investable / buy_price
                entry_price = buy_price
                entry_date = date
                capital = 0.0

            # Calcolo valore portafoglio
            current_val = capital if position == 0 else position * close
            equity_curve.append(current_val)

        equity_series = pd.Series(equity_curve, index=data.index)
        trades_df = pd.DataFrame(trades)
        return equity_series, trades_df, data