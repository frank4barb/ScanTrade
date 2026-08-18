"""
ScanTrade - ETF Trading Strategy Finder & Simulator
Punto di ingresso principale del sistema.
"""

import sys

def print_project_info():
    print("=" * 70)
    print(" 📈 ScanTrade - Search & Simulation Engine per ETF")
    print("=" * 70)
    print(" Obiettivo:  Identificazione e backtesting di strategie ottimali su ETF")
    print(" Versione:   0.1.0")
    print(" Python:    ", sys.version.split()[0])
    print("=" * 70)
    
    print("\n💡 DESCRIZIONE DEL PROGETTO:")
    print(" ScanTrade permette di analizzare serie storiche di ETF, identificare")
    print(" automazioni/regole di trading profittevoli ed eseguirne una simulazione")
    print(" rigorosa (backtest) valutando rendimento e rischio rettificato.")
    
    print("\n🧩 ARCHITETTURA DEL SISTEMA:")
    print(" 1. [Data Engine]        Download storico quotazioni & calcolo indicatori (RSI, SMA, MACD, ATR)")
    print(" 2. [Strategy Engine]    Definizione regole di BUY/SELL e gestione rischio (Stop Loss / Take Profit)")
    print(" 3. [Strategy Finder]    Ottimizzazione parametri (Grid Search / Algoritmi Genetici / Walk-Forward)")
    print(" 4. [Backtest Engine]    Simulazione storica con capitale, commissioni, slippage e tracking dell'equity")
    print(" 5. [Analytics Engine]   Metriche chiave (Sharpe, Sortino, Max Drawdown, Win Rate, Profit Factor)")
    print(" 6. [Reporter]           Generazione report prestazionali ed Equity Curve")
    
    print("\n📌 STATO ATTUALE:")
    print(" - Struttura di base e documentazione completate.")
    print(" - Pronti per l'implementazione del modulo Data Fetcher & Indicatori.\n")
    print("=" * 70)

if __name__ == "__main__":
    print_project_info()