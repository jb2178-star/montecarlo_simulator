import os
import json
from datastructures import HashTable

CACHE_FILE = 'sp500_data_cache.json'

def load_cache():
    if not os.path.exists(CACHE_FILE):
        return None
    with open(CACHE_FILE, 'r') as f:
        cached_data = json.load(f)
    stocks_table = HashTable()
    for ticker, data in cached_data.items():
        stocks_table.set(ticker, data)
    return stocks_table

def save_cache(stocks_table):
    serializable_data = {ticker: data for ticker, data in stocks_table.items()}
    with open(CACHE_FILE, 'w') as f:
        json.dump(serializable_data, f, indent=2)
