from datastructures import HashTable
from sample_stocks.sp500_fetch import fetch_sp500_tickers_and_sectors, fetch_annual_volatility, fetch_last_close_price
from sample_stocks.sp500_cache import load_cache, save_cache

def build_sp500_data():
    tickers_sectors = fetch_sp500_tickers_and_sectors()
    stocks_table = HashTable()

    for idx, row in tickers_sectors.iterrows():
        ticker = row['Symbol']
        sector = row['GICS Sector']
        volatility = fetch_annual_volatility(ticker)
        last_close = fetch_last_close_price(ticker)

        if volatility is None or last_close is None:
            print(f"Skipping {ticker}: missing volatility or last_close")
            continue

        stocks_table.set(ticker, {
            'sector': sector,
            'volatility': float(volatility),
            'last_close': last_close
        })

    save_cache(stocks_table)
    return stocks_table

def get_sp500_data():
    stocks = load_cache()
    if stocks is None:
        print("Cache not found, building data. This may take some time...")
        stocks = build_sp500_data()
    else:
        print("Loaded S&P 500 data from cache.")
    return stocks

if __name__ == "__main__":
    stocks = get_sp500_data()
    print(f"Loaded {len(stocks)} stocks into HashTable.")
