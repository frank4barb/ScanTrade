# Specifiche Progetto: ScanTrade

## Descrizione Iniziale
L'obiettivo del progetto è realizzare un programma che cerca (e poi simula) una formula di compravendita di ETF in grado di massimizzare il profitto.

## Storico Modifiche
- **Inizializzazione del progetto**: Creazione della documentazione di base (`README.md`, `SPEC.md`) e dello script di avvio (`main.py`).
- Modifica: mi dai informazioni su questo progetto?
  Dettagli: Creata la struttura iniziale del repository con documentazione informativa (README.md), tracciamento specifiche (SPEC.md) e punto di ingresso base (main.py).

- Modifica: /quit
  Dettagli: - Modifica: Chiusura sessione (/quit)
  Dettagli: Ricevuto comando di uscita. Nessuna modifica apportata ai file del progetto.

- Modifica: mi descrivi il progetto?
  Dettagli: - Modifica: Richiesta descrizione dettagliata del progetto
  Dettagli: Fornita spiegazione esaustiva dell'architettura e degli obiettivi di ScanTrade e aggiornato `main.py` con una descrizione estesa dei moduli e del flusso operativo del sistema.

- Modifica: mi descrivi il progetto?
  Dettagli: - Modifica: Richiesta descrizione dettagliata del progetto
  Dettagli: Fornita spiegazione esaustiva dell'architettura e degli obiettivi di ScanTrade e aggiornato `main.py` e `README.md` con la panoramica sui moduli del sistema.

- Modifica: mi riassumi il contenuto del progetto?
  Dettagli: - Modifica: Richiesta riassunto del progetto
  Dettagli: Fornita una sintesi dettagliata degli obiettivi, dell'architettura dei moduli e dello stato attuale del progetto ScanTrade.

- Modifica: puoi generare il codice python che risponde alle specifiche del progetto in un foglio Jupyter Notebook e aggiornare git?
  Dettagli: - Modifica: Creazione del Jupyter Notebook `ScanTrade.ipynb` con il codice completo per tutti i moduli del sistema (Data Engine, Strategy Engine, Backtest Engine, Strategy Finder e Analytics Engine) e aggiornamento della documentazione in `README.md`.
  Dettagli: Generato `ScanTrade.ipynb` contenente le classi Python complete per download dati, calcolo indicatori (SMA, EMA, RSI, MACD, ATR), generazione segnali di trading con Stop Loss / Take Profit, simulazione barra per barra del backtest con commissioni/slippage, ottimizzazione tramite Grid Search e generazione di metriche prestazionali con dashboard visuale.

- Modifica: non vedo nessun aggiornamento sul progetto ScanTrade di github. puoi verificare?
  Dettagli: - Modifica: Implementazione dei moduli Python eseguibili del framework ScanTrade e aggiornamento di `main.py`.
  Dettagli: Creati i file Python `data_engine.py`, `strategy_engine.py`, `backtest_engine.py`, `analytics_engine.py` e `strategy_finder.py`. Aggiornato `main.py` per eseguire in automatico il flusso completo: caricamento dati ETF, ricerca Grid Search della miglior combinazione di parametri, backtesting con gestione costi e generazione report/grafico prestazionale (`scantrade_performance.png`).

- Modifica: mi riassumi le funzioni del progetto?
  Dettagli: Fornita una panoramica dettagliata ed esaustiva di tutte le funzioni, classi e moduli che compongono il framework ScanTrade.

- Modifica: suggerimento supporto esecuzione Jupyter Notebook su Chromebook
  Dettagli: Fornita guida passo-passo per l'esecuzione di ScanTrade.ipynb su Chromebook utilizzando Google Colab, Binder e l'ambiente Linux integrato (Crostini).
- Modifica: ho visto il file Notebook Jupyter su github, ma non riesco ad eseguirlo. puoi suggerirmi come posso fare visto che sto usando un chromebook?
  Dettagli: Aggiunta nota in SPEC.md per il supporto e le opzioni di esecuzione di ScanTrade.ipynb su Chromebook.

- Modifica: puoi rendere pubblico il repository?
  Dettagli: Fornite istruzioni per impostare la visibilità del repository su "Public" tramite le impostazioni di GitHub / GitHub CLI e verificata l'assenza di dati sensibili nei file di progetto.
- Modifica: puoi rendere pubblico il repository?
  Dettagli: Aggiunto allo storico delle modifiche in SPEC.md il riferimento alle istruzioni per rendere pubblico il repository GitHub.
