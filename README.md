# ScanTrade 📈

**ScanTrade** è un framework in Python ideato per la ricerca, ottimizzazione e simulazione (backtesting) di formule e strategie di compravendita su ETF, volte alla massimizzazione del profitto e alla gestione del rischio.

## 🚀 Obiettivi del Progetto
- **Ricerca Automatica di Strategie**: Identificazione delle migliori regole di ingresso/uscita mediante parametri tecnici e strategie quantitative.
- **Backtesting Accurato**: Simulazione storica considerando capitale iniziale, commissioni, slippage e gestione del rischio (Stop Loss / Take Profit).
- **Analisi delle Performance**: Calcolo di indicatori chiave (ROI, Sharpe Ratio, Sortino Ratio, Max Drawdown, Win Rate, Profit Factor).

## 🛠️ Architettura dei Moduli
- `data_engine.py`: Fetching serie storiche e calcolo indicatori tecnici (RSI, SMA/EMA, MACD, ATR).
- `strategy_engine.py`: Regole operative di Buy/Sell e regole di Risk Management.
- `backtest_engine.py`: Simulazione barra-per-barra con gestione del portafoglio e costi di transazione.
- `strategy_finder.py`: Algoritmi di ricerca e ottimizzazione parametri (Grid Search).
- `analytics_engine.py`: Report dettagliati, metriche economico-finanziarie e grafici prestazionali (Equity Curve, Drawdown).
- `main.py`: Punto di ingresso eseguibile da riga di comando per l'intero workflow.

## 📓 Notebook Interattivo
Tutti i moduli del framework e il flusso di simulazione end-to-end sono disponibili anche in forma interattiva nel Jupyter Notebook:
- [`ScanTrade.ipynb`](ScanTrade.ipynb)

## 📦 Installazione e Avvio
```bash
# Esecuzione completa del motore da riga di comando
python main.py

# Avvio del Jupyter Notebook interattivo
jupyter notebook ScanTrade.ipynb
```