import numpy as np

def monte_carlo_simulation(stock_data, days=30): 
    current_price = stock_data.get('last_close') or 0
    volatility = stock_data.get('volatility') or 0

    if current_price == 0 or volatility == 0:
        return None, []

    prices = [current_price]
    returns = []
    for _ in range(days):
        daily_return = np.random.normal(0, volatility / np.sqrt(252))
        new_price = prices[-1] * (1 + daily_return)
        prices.append(new_price)
        returns.append(daily_return)

    final_price = prices[-1]
    return final_price, prices, returns
