"""
ScanTrade - Strategy Finder
Ricerca ed ottimizzazione parametri mediante Grid Search.
"""

import itertools
import pandas as pd
from strategy_engine import StrategyEngine
from backtest_engine import BacktestEngine
from analytics_engine import AnalyticsEngine

class StrategyFinder:
    def __init__(self, df, backtester=None):
        self.df = df
        self.backtester = backtester or BacktestEngine()

    def grid_search(self, fast_range=[10, 20, 30], slow_range=[40, 60, 100], sl_range=[0.02, 0.04], tp_range=[0.06, 0.10]):
        results = []
        combinations = list(itertools.product(fast_range, slow_range, sl_range, tp_range))
        print(f"🔍 Avvio Grid Search su {len(combinations)} combinazioni di parametri...")
        
        for fast, slow, sl, tp in combinations:
            if fast >= slow:
                continue
            strategy = StrategyEngine(fast_window=fast, slow_window=slow, stop_loss_pct=sl, take_profit_pct=tp)
            equity, trades, _ = self.backtester.run(self.df, strategy)
            metrics = AnalyticsEngine.calculate_metrics(equity, trades, self.backtester.initial_capital)
            
            if metrics:
                results.append({
                    'Fast Window': fast,
                    'Slow Window': slow,
                    'Stop Loss': sl,
                    'Take Profit': tp,
                    'Total Return (%)': metrics['Total Return (%)'],
                    'Sharpe Ratio': metrics['Sharpe Ratio'],
                    'Max Drawdown (%)': metrics['Max Drawdown (%)'],
                    'Win Rate (%)': metrics['Win Rate (%)'],
                    'Trades': metrics['Total Trades']
                })
                
        results_df = pd.DataFrame(results)
        if not results_df.empty:
            results_df = results_df.sort_values(by='Sharpe Ratio', ascending=False).reset_index(drop=True)
        return results_df