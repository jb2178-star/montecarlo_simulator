import yfinance as yf
import numpy as np
import pandas as pd

def fetch_sp500_tickers_and_sectors():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    table = pd.read_html(url, header=0)[0]
    return table[['Symbol', 'GICS Sector']]

def fetch_annual_volatility(ticker, period='1y'):
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period)['Close']
        if hist.empty:
            print(f"Warning: No historical data for volatility for {ticker}")
            return None
        log_returns = np.log(hist / hist.shift(1)).dropna()
        daily_volatility = log_returns.std()
        annual_volatility = daily_volatility * np.sqrt(252)
        return annual_volatility
    except Exception as e:
        print(f"Error fetching volatility for {ticker}: {e}")
        return None

def fetch_last_close_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period='2d')
        if hist.empty:
            print(f"Warning: No historical data for price for {ticker}")
            return None
        if len(hist) < 2:
            last_close = hist['Close'].iloc[-1]
        else:
            last_close = hist['Close'].iloc[-2]
        return float(last_close)
    except Exception as e:
        print(f"Error fetching last close for {ticker}: {e}")
        return None
