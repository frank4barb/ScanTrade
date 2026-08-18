"""
ScanTrade - Analytics Engine
Calcolo indicatori finanziari di performance e generazione grafici.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class AnalyticsEngine:
    @staticmethod
    def calculate_metrics(equity_series, trades_df, initial_capital=10000.0):
        if equity_series.empty or len(equity_series) < 2:
            return {}
            
        total_return = (equity_series.iloc[-1] - initial_capital) / initial_capital * 100
        days = (equity_series.index[-1] - equity_series.index[0]).days
        years = max(days / 365.25, 0.01)
        cagr = (((equity_series.iloc[-1] / initial_capital) ** (1 / years)) - 1) * 100
        
        daily_returns = equity_series.pct_change().dropna()
        sharpe_ratio = (daily_returns.mean() / (daily_returns.std() + 1e-10)) * np.sqrt(252)
        
        downside_returns = daily_returns[daily_returns < 0]
        sortino_ratio = (daily_returns.mean() / (downside_returns.std() + 1e-10)) * np.sqrt(252)
        
        cummax = equity_series.cummax()
        drawdowns = (equity_series - cummax) / cummax * 100
        max_drawdown = drawdowns.min()
        
        num_trades = len(trades_df)
        if num_trades > 0:
            win_trades = trades_df[trades_df['PnL (%)'] > 0]
            win_rate = len(win_trades) / num_trades * 100
            
            gross_profit = trades_df[trades_df['PnL (%)'] > 0]['PnL (%)'].sum()
            gross_loss = abs(trades_df[trades_df['PnL (%)'] < 0]['PnL (%)'].sum())
            profit_factor = gross_profit / gross_loss if gross_loss > 0 else np.nan
        else:
            win_rate = 0.0
            profit_factor = 0.0
            
        return {
            'Total Return (%)': round(total_return, 2),
            'CAGR (%)': round(cagr, 2),
            'Sharpe Ratio': round(sharpe_ratio, 2),
            'Sortino Ratio': round(sortino_ratio, 2),
            'Max Drawdown (%)': round(max_drawdown, 2),
            'Win Rate (%)': round(win_rate, 2),
            'Profit Factor': round(profit_factor, 2) if not np.isnan(profit_factor) else "N/A",
            'Total Trades': num_trades
        }

    @staticmethod
    def plot_dashboard(df, equity_series, trades_df, title="ScanTrade Performance Dashboard", save_path=None):
        plt.figure(figsize=(14, 10))
        
        # Subplot 1: Prezzo e Segnali
        ax1 = plt.subplot(3, 1, 1)
        ax1.plot(df.index, df['Close'], label='ETF Close Price', color='black', alpha=0.75)
        if 'SMA_Fast' in df.columns:
            ax1.plot(df.index, df['SMA_Fast'], label='SMA Fast', color='blue', linestyle='--')
        if 'SMA_Slow' in df.columns:
            ax1.plot(df.index, df['SMA_Slow'], label='SMA Slow', color='orange', linestyle='--')
            
        if not trades_df.empty:
            ax1.scatter(trades_df['Entry Date'], trades_df['Entry Price'], marker='^', color='green', s=80, label='Buy', zorder=5)
            ax1.scatter(trades_df['Exit Date'], trades_df['Exit Price'], marker='v', color='red', s=80, label='Sell', zorder=5)
            
        ax1.set_title(f"{title} - Prezzo ETF e Trade", fontsize=12, fontweight='bold')
        ax1.set_ylabel("Prezzo ($)")
        ax1.legend(loc='upper left')
        ax1.grid(True, alpha=0.3)
        
        # Subplot 2: Equity Curve vs Benchmark
        ax2 = plt.subplot(3, 1, 2, sharex=ax1)
        buy_hold = (df['Close'] / df['Close'].iloc[0]) * equity_series.iloc[0]
        ax2.plot(equity_series.index, equity_series, label='ScanTrade Strategy Equity', color='green', linewidth=2)
        ax2.plot(buy_hold.index, buy_hold, label='Benchmark Buy & Hold', color='gray', linestyle=':', linewidth=1.5)
        ax2.set_title("Evoluzione Capitale ($)", fontsize=12, fontweight='bold')
        ax2.set_ylabel("Valore ($)")
        ax2.legend(loc='upper left')
        ax2.grid(True, alpha=0.3)
        
        # Subplot 3: Drawdown
        ax3 = plt.subplot(3, 1, 3, sharex=ax1)
        cummax = equity_series.cummax()
        drawdown = (equity_series - cummax) / cummax * 100
        ax3.fill_between(drawdown.index, drawdown, 0, color='red', alpha=0.3, label='Drawdown %')
        ax3.set_title("Drawdown Curve (%)", fontsize=12, fontweight='bold')
        ax3.set_ylabel("Drawdown %")
        ax3.legend(loc='lower left')
        ax3.grid(True, alpha=0.3)
        
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path)
            print(f"📊 Grafico salvato in: {save_path}")
        else:
            plt.show()