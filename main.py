"""
ScanTrade - ETF Trading Strategy Finder & Simulator
Punto di ingresso principale del sistema.
"""

import sys
from data_engine import DataEngine
from strategy_engine import StrategyEngine
from backtest_engine import BacktestEngine
from strategy_finder import StrategyFinder
from analytics_engine import AnalyticsEngine

def main():
    print("=" * 70)
    print(" 📈 ScanTrade - Search & Simulation Engine per ETF")
    print("=" * 70)
    print(" Obiettivo:  Identificazione e backtesting di strategie ottimali su ETF")
    print(" Versione:   1.0.0")
    print(" Python:    ", sys.version.split()[0])
    print("=" * 70)
    
    symbol = "SPY"
    print(f"\n📥 [1/4] Caricamento dati storici ETF ({symbol})...")
    df = DataEngine.fetch_etf_data(symbol=symbol, period="3y")
    print(f"   ✓ Caricate {len(df)} barre dal {df.index[0].strftime('%Y-%m-%d')} al {df.index[-1].strftime('%Y-%m-%d')}")
    
    print("\n🔍 [2/4] Avvio modulo Strategy Finder (Grid Search Optimization)...")
    finder = StrategyFinder(df)
    results = finder.grid_search(
        fast_range=[10, 20, 30],
        slow_range=[40, 60, 90],
        sl_range=[0.03, 0.05],
        tp_range=[0.08, 0.12]
    )
    
    if results.empty:
        print("⚠️ Nessun risultato valido trovato durante la ricerca.")
        return

    print("\n🏆 Top 3 Strategie Individuate:")
    print(results.head(3).to_string(index=False))
    
    best = results.iloc[0]
    print(f"\n⚙️ [3/4] Esecuzione Backtest con la strategia migliore (Sharpe: {best['Sharpe Ratio']})...")
    best_strategy = StrategyEngine(
        fast_window=int(best['Fast Window']),
        slow_window=int(best['Slow Window']),
        stop_loss_pct=best['Stop Loss'],
        take_profit_pct=best['Take Profit']
    )
    
    backtester = BacktestEngine(initial_capital=10000.0, commission_pct=0.001)
    equity, trades, df_signals = backtester.run(df, best_strategy)
    
    metrics = AnalyticsEngine.calculate_metrics(equity, trades)
    print("\n📊 [4/4] METRICHE DI PERFORMANCE FINALI:")
    for metric_name, value in metrics.items():
        print(f"   • {metric_name:<20}: {value}")
        
    print("\n📈 Generazione grafico della dashboard prestazionale...")
    AnalyticsEngine.plot_dashboard(
        df_signals, 
        equity, 
        trades, 
        title=f"ScanTrade Best Strategy ({symbol})",
        save_path="scantrade_performance.png"
    )
    print("\n✅ Esecuzione completata con successo! Puoi esplorare anche il Jupyter Notebook 'ScanTrade.ipynb'.\n")

if __name__ == "__main__":
    main()