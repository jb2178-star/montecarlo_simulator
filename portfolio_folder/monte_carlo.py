from monte_carlo import monte_carlo_simulation
def monte_carlo_all(self, days=30):
        for bucket in self.stocks.table:
            for ticker, stock_data in bucket:
                if isinstance(stock_data, dict):  #if stock in hashtable
                    result = monte_carlo_simulation(stock_data, days)  #run monte carlo simulation
                    if result is None:
                        continue
                    final_price, prices, returns = result
                    self.simulated_returns.set(ticker, returns)  #hashtable lookups, update stock data
                    stock_data['last_close'] = final_price
                    self.stocks.set(ticker, stock_data)  #hashtable store simulated results for hashtable look up
                    self.price_tree.insert(ticker, final_price)  #BST inorder transveral, stocks sorted by price
        self.record_port()
        self.update_returns_tr()