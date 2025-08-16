from datastructures import Stack
def buy_stock(self, ticker, shares):
        price_data = self.stocks.get(ticker) #hash table lookup, returns dict
        if not price_data:
            return f"Stock {ticker} not found!"
        price = price_data.get('last_close', 0)
        cost = shares * price
        if cost > self.cash:
            return f"Not enough cash to buy {shares} shares of {ticker}. Need ${cost:.2f}, have ${self.cash:.2f}"

        current_shares = self.positions.get(ticker) or 0
        self.positions.set(ticker, current_shares + shares) #hashtable update positions
        self.cash -= cost  
        transaction = f"BUY {shares} {ticker} @ ${price:.2f}"
        self.history.append(transaction) #linkedlist add transaction
        self.undo_stack.push(("BUY", ticker, shares, price)) #push action onto stack
        self.redo_stack = Stack()  #clear redo history on new action
        self.record_cash()
        self.record_port()  #record value after transaction
        return f"Bought {shares} shares of {ticker} for ${cost:.2f}"

def sell_stock(self, ticker, shares):
        current_shares = self.positions.get(ticker) or 0 #hash table lookup
        if current_shares < shares:
            return f"Not enough shares! You have {current_shares}"
        price_data = self.stocks.get(ticker) #hashtable lookup
        if not price_data:
            return f"Stock {ticker} not found!"
        price = price_data.get('last_close', 0)
        self.positions.set(ticker, current_shares - shares) #hashtable update positions
        revenue = shares * price
        self.cash += revenue  #add cash back
        transaction = f"SELL {shares} {ticker} @ ${price:.2f}"
        self.history.append(transaction) #linkedlist add transaction
        self.undo_stack.push(("SELL", ticker, shares, price))
        self.record_cash()
        self.record_port()  #record value after transaction
        return f"Sold {shares} shares of {ticker} for ${revenue:.2f}"

def undo_last_transaction(self): 
        if self.undo_stack.is_empty():
            return "Nothing to undo"
        action_type, ticker, shares, price = self.undo_stack.pop()
        current_shares = self.positions.get(ticker) or 0

        if action_type == "BUY":
            self.positions.set(ticker, max(0, current_shares - shares)) #undo buy = remove shares, refund cash
            refund = shares * price
            self.cash += refund
            undo_msg = f"Undid BUY: Removed {shares} shares of {ticker}, refunded ${refund:.2f} to cash"
        else:
            self.positions.set(ticker, current_shares + shares) #undo sell = add shares back, deduct cash
            cost = shares * price
            if self.cash < cost:
                undo_msg = f"Cannot undo SELL due to insufficient cash." #not enough cash to undo sell
            else:
                self.cash -= cost
                undo_msg = f"Undid SELL: Added back {shares} shares of {ticker}, deducted ${cost:.2f} from cash"
        self.redo_stack.push((action_type, ticker, shares, price))  #stack push undone action to redo
        self.record_cash()
        self.record_port()
        return undo_msg

def redo_last_transaction(self):
        if self.redo_stack.is_empty():
            return "Nothing to redo"
        action_type, ticker, shares, price = self.redo_stack.pop()
        current_shares = self.positions.get(ticker) or 0
        if action_type == "BUY":
            cost = shares * price
            if cost > self.cash:
                return f"Cannot redo BUY: Not enough cash (${self.cash:.2f}) to buy {shares} shares of {ticker} (cost ${cost:.2f})"
            self.positions.set(ticker, current_shares + shares)
            self.cash -= cost
            redo_msg = f"Redid BUY: Added {shares} shares of {ticker}, spent ${cost:.2f}"
        else:
            if current_shares < shares:
                return f"Cannot redo SELL: Not enough shares to sell (have {current_shares})"
            self.positions.set(ticker, current_shares - shares)
            revenue = shares * price
            self.cash += revenue
            redo_msg = f"Redid SELL: Removed {shares} shares of {ticker}, gained ${revenue:.2f}"
        self.undo_stack.push((action_type, ticker, shares, price))  #stack push back onto undo stack
        self.record_cash()
        self.record_port()
        return redo_msg