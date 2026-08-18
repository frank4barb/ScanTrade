"""
ScanTrade - ETF Trading Strategy Finder & Simulator
Punto di ingresso principale del sistema.
"""

import sys

def print_project_info():
    print("=" * 60)
    print(" 📈 ScanTrade - Search & Simulation Engine per ETF")
    print("=" * 60)
    print("Obiettivo: Ricerca e simulazione di strategie di trading su ETF")
    print("Versione:   0.1.0 (Iniziale)")
    print("Python:    ", sys.version.split()[0])
    print("=" * 60)
    print("\nStruttura prevista dei moduli:")
    print(" 1. Data Fetcher & Indicatori Tecnici")
    print(" 2. Strategy Finder / Optimizer (Grid Search, Genetico)")
    print(" 3. Backtesting Engine & Simulatore")
    print(" 4. Report & Visualizzazione Performance\n")

if __name__ == "__main__":
    print_project_info()