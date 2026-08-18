# ScanTrade 📈

**ScanTrade** è un framework in Python ideato per la ricerca, ottimizzazione e simulazione (backtesting) di formule e strategie di compravendita su ETF, volte alla massimizzazione del profitto e alla gestione del rischio.

## 🚀 Obiettivi del Progetto
- **Ricerca Automatica di Strategie**: Identificazione delle migliori regole di ingresso/uscita mediante parametri tecnici e strategie quantitative.
- **Backtesting Accurato**: Simulazione storica considerando capitale iniziale, commissioni, slippage e gestione del rischio (Stop Loss / Take Profit).
- **Analisi delle Performance**: Calcolo di indicatori chiave (ROI, Sharpe Ratio, Sortino Ratio, Max Drawdown, Win Rate, Profit Factor).

## 🛠️ Architettura dei Moduli
- `Data Engine`: Fetching serie storiche e calcolo indicatori tecnici (RSI, SMA/EMA, MACD, ATR).
- `Strategy Engine`: Regole operative di Buy/Sell e regole di Risk Management.
- `Strategy Finder`: Algoritmi di ricerca e ottimizzazione parametri (Grid Search, Algoritmi Genetici).
- `Backtest Engine`: Simulazione barra-per-barra con gestione del portafoglio e costi di transazione.
- `Analytics & Reporting`: Report dettagliati e grafici prestazionali (Equity Curve, Drawdown).

## 📦 Installazione e Avvio
```bash
python main.py
```