import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


def prepare_data_for_pca(stocks_hashtable, returns_hashtable):
    data = []
    tickers = []

    for bucket in stocks_hashtable.table: #iterate over all buckets in stocks hashtable
        for ticker, stock_data in bucket: #each bucket cotains ticker, stock pairs
            if not isinstance(stock_data, dict): #ensure stock data is dict
                continue
            sector = stock_data.get('sector') #extract sector and volatility for current stock
            volatility = stock_data.get('volatility')
            returns = returns_hashtable.get(ticker) #get returns
            if returns is None or len(returns) == 0: #skip if no returns
                continue
            avg_return = np.mean(returns)#compute average return

            tickers.append(ticker)#append ticker
            data.append({
                'sector': sector,
                'volatility': volatility,
                'avg_return': avg_return
            })

    df = pd.DataFrame(data, index=tickers) #convert list of feature dicts to dataframe
    sector_encoded = pd.get_dummies(df['sector'])
    df = df.drop(columns=['sector']) #add encoded sector
    df = pd.concat([df, sector_encoded], axis=1)

    scaler = StandardScaler() #scale features to zero mean
    X_scaled = scaler.fit_transform(df)

    return tickers, X_scaled, df.columns.tolist()

def do_pca(X_scaled, n_components=2):
    
    U, S, VT = np.linalg.svd(X_scaled, full_matrices=False)#perform SVD
    pcs = U @ np.diag(S)#compute principal components (scores)
    pcs = pcs[:, :n_components]#keep only the first n_components
    explained_variance = (S ** 2) / (X_scaled.shape[0] - 1)#compute explained variance ratio
    explained_variance_ratio = explained_variance / explained_variance.sum()
    return pcs, explained_variance_ratio[:n_components]

def get_pca_results(stocks_hashtable, returns_hashtable, n_components=2):
    tickers, X_scaled, features = prepare_data_for_pca(stocks_hashtable, returns_hashtable)
    pcs, evr = do_pca(X_scaled, n_components)
    return tickers, pcs, evr, features
def get_sectors(stocks_hashtable, tickers):
    sectors = []
    for ticker in tickers:
        stock_data = stocks_hashtable.get(ticker)
        if stock_data and isinstance(stock_data, dict):
            sectors.append(stock_data.get('sector', 'Unknown'))
        else:
            sectors.append('Unknown')
    return sectors
def get_1d_pca_results(stocks_hashtable, returns_hashtable):
    tickers, X_scaled, features = prepare_data_for_pca(stocks_hashtable, returns_hashtable)
    pcs, evr = do_pca(X_scaled, n_components=1)
    sectors = get_sectors(stocks_hashtable, tickers)
    return tickers, pcs[:, 0], sectors, evr[0]