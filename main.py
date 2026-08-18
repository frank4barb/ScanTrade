"""
ScanTrade - ETF Trading Strategy Finder & Simulator
Punto di ingresso principale del sistema.
"""

import sys

def print_project_info():
    print("=" * 68)
    print(" 📈 ScanTrade - Search & Simulation Engine per ETF")
    print("=" * 68)
    print(" Obiettivo:  Identificazione e backtesting di strategie ottimali su ETF")
    print(" Versione:   0.1.0")
    print(" Python:    ", sys.version.split()[0])
    print("=" * 68)
    
    print("\n💡 DESCRIZIONE DEL PROGETTO:")
    print(" ScanTrade permette di analizzare serie storiche di ETF, identificare")
    print(" automazioni/regole di trading profittevoli ed eseguirne una simulazione")
    print(" rigorosa (backtest) valutando rendimento e rischio.")
    
    print("\n🧩 ARCHITETTURA DEL SISTEMA:")
    print(" 1. [Data Fetcher]      Download storico quotazioni & calcolo indicatori (RSI, SMA, MACD, ATR)")
    print(" 2. [Strategy Engine]   Definizione regole di BUY/SELL e gestione rischio (Stop Loss / Take Profit)")
    print(" 3. [Strategy Finder]   Ottimizzazione parametri tramite Grid Search o Algoritmi Genetici")
    print(" 4. [Backtest Engine]   Simulazione storica con capitale, commissioni, slippage e metriche (Sharpe, Drawdown)")
    print(" 5. [Reporter]          Generazione report prestazionali e grafici d'andamento")
    
    print("\n📌 STATO ATTUALE:")
    print(" - Estruttura di base completata.")
    print(" - Pronti per l'implementazione del modulo Data Fetcher & Indicatori.\n")
    print("=" * 68)

if __name__ == "__main__":
    print_project_info()