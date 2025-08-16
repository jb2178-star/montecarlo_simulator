
def record_portfolio_value(self):#record current portfolio value using LinkedList
        _, stock_value = self.show_port()
        total_value = stock_value + self.cash
        self.value_history.append(total_value) #linkedlist appened value for tracking
        return total_value
def show_portfolio(self):
        output = []
        total_value = 0
        for bucket in self.positions.table: #hashtable iteration over positions
            for ticker, shares in bucket:
                if shares and shares > 0: 
                    price_data = self.stocks.get(ticker) or {}
                    price = price_data.get('last_close', 0)
                    value = shares * price
                    total_value += value
                    output.append(f"{ticker}: {shares} shares @ ${price:.2f} = ${value:.2f}")
        output.append(f"Cash: ${self.cash:.2f}")
        return output, total_value