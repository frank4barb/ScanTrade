"""
ScanTrade - Data Engine
Gestione acquisizione serie storiche ETF e calcolo indicatori tecnici.
"""

import numpy as np
import pandas as pd

class DataEngine:
    @staticmethod
    def generate_synthetic_etf_data(days=1000, start_price=100.0, seed=42):
        np.random.seed(seed)
        dates = pd.date_range(end=pd.Timestamp.today(), periods=days, freq='B')
        returns = np.random.normal(0.0004, 0.015, days)
        price = start_price * np.exp(np.cumsum(returns))
        
        high = price * (1 + np.abs(np.random.normal(0, 0.008, days)))
        low = price * (1 - np.abs(np.random.normal(0, 0.008, days)))
        open_p = low + (high - low) * np.random.uniform(0.2, 0.8, days)
        close = price
        volume = np.random.randint(100000, 5000000, days)
        
        df = pd.DataFrame({
            'Open': open_p,
            'High': high,
            'Low': low,
            'Close': close,
            'Volume': volume
        }, index=dates)
        return df

    @staticmethod
    def fetch_etf_data(symbol="SPY", period="3y"):
        try:
            import yfinance as yf
            df = yf.download(symbol, period=period, progress=False)
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)
            if df.empty:
                raise ValueError("Nessun dato scaricato.")
            return df
        except Exception as e:
            print(f"⚠️ Impossibile scaricare dati con yfinance ({e}). Generazione dati sintetici per {symbol}...")
            return DataEngine.generate_synthetic_etf_data()

    @staticmethod
    def add_indicators(df, fast_sma=20, slow_sma=50, rsi_period=14, atr_period=14):
        df = df.copy()
        df['SMA_Fast'] = df['Close'].rolling(window=fast_sma).mean()
        df['SMA_Slow'] = df['Close'].rolling(window=slow_sma).mean()
        df['EMA_Fast'] = df['Close'].ewm(span=fast_sma, adjust=False).mean()
        df['EMA_Slow'] = df['Close'].ewm(span=slow_sma, adjust=False).mean()
        
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=rsi_period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=rsi_period).mean()
        rs = gain / (loss + 1e-10)
        df['RSI'] = 100 - (100 / (1 + rs))
        
        ema12 = df['Close'].ewm(span=12, adjust=False).mean()
        ema26 = df['Close'].ewm(span=26, adjust=False).mean()
        df['MACD'] = ema12 - ema26
        df['MACD_Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()
        
        high_low = df['High'] - df['Low']
        high_close = (df['High'] - df['Close'].shift()).abs()
        low_close = (df['Low'] - df['Close'].shift()).abs()
        tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
        df['ATR'] = tr.rolling(window=atr_period).mean()
        return df