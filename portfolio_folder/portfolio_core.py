from datastructures import HashTable, LinkedList, Queue, Stack, BST, Graph
from sample_stocks.sp500_data import get_sp500_data, build_sp500_data
from portfolio_folder.graph_utli import update_graph_with_correlations, get_networkx_graph
from portfolio_folder.transactions import buy_stock, sell_stock, redo_last_transaction, undo_last_transaction
from portfolio_folder.monte_carlo import monte_carlo_all
from portfolio_folder.show_record_port import record_portfolio_value, show_portfolio
from portfolio_folder.portfolio_analysis import get_portfolio_change, get_portfolio_values, get_stock_rankings, update_returns_tree, get_stock_rankings_by_return, merge_sort_stocks

class Portfolio:
    def __init__(self, initial_cash=10000.0):
        self.stocks = HashTable() #hashtable mapping ticker
        self.positions = HashTable() #hashtable mapping ticker
        self.history = LinkedList() #linkedlist to store transaction history
        self.undo_stack = Stack() #stack to hold undo history, stores actions
        self.redo_stack= Stack() #stack to hold redo history
        self.pending_orders = Queue() #not implemented yet
        self.price_tree = BST() #BST to keep stocks sorted by price for efficient ranking retrieval
        self.stock_network = Graph() #graph for stock correlations with weights
        self.simulated_returns = HashTable() #store returns for each ticker
        self.load_sample_stocks() #initialize sample stocks
        self.value_history = LinkedList()  #LinkedList for value tracking
        self.cash = initial_cash #current cash in portfolio
        self.cash_history = LinkedList()  #linkedlist to track cash history
        self.record_cash()
        #self.simulation_days = 0
        self.returns_tree = BST()  #BST keyed by cumulative return
        
        

    def load_fresh_stocks(self):#directly build from Wikipedia/YFinance
        self.stocks = build_sp500_data()  #always returns new data
        for bucket in self.stocks.table:
            for ticker, data in bucket:
                price = data.get('last_close', 0)
                self.price_tree.insert(ticker, price)
                self.stock_network.add_vertex(ticker)
    def record_cash(self):
        self.cash_history.append(self.cash) #linkedlist append current cash amount to cashhistory
    def set_cash(self, amount):
        self.cash = amount
        self.record_cash()
    def get_all_tickers(self):
        tickers = []  #initialize empty list to hold tickers
        for bucket in self.stocks.table:
            for ticker, data in bucket:
                tickers.append(ticker)  #add ticker to list
        return tickers
    def load_sample_stocks(self):
        self.stocks = get_sp500_data()#load S&P 500 data from sample_stocks.py
        for bucket in self.stocks.table:#insert stocks and prices into price_tree and add vertices to graph
            for ticker, data in bucket:
                price = data.get('last_close', 0)#data is a dict with 'last_close' and 'volatility'
                self.price_tree.insert(ticker, price)
                self.stock_network.add_vertex(ticker)
    def get_portfolio_chan(self):
        return get_portfolio_change(self)
    def get_portfolio_val(self):
        return get_portfolio_values(self)
    def get_stock_rank(self):
        return get_stock_rankings(self)
    def update_returns_tr(self):
        return update_returns_tree(self)
    def record_port(self):
        return record_portfolio_value(self)
    def show_port(self):
        return show_portfolio(self)
    def show_transaction_history(self):
        transactions = []
        current = self.history.head #linked list traversal from head
        while current:
            transactions.append(current.data)
            current = current.next
        return transactions
    def update_stock_price(self, ticker, new_price): #update stock price from Monte Carlo simulation
        price_data = self.stocks.get(ticker)
        if price_data and isinstance(price_data, dict):
            price_data['last_close'] = new_price
            self.stocks.set(ticker, price_data)  #hashtable update price
            self.price_tree.insert(ticker, new_price)
    def get_stock_rankings_by_ret(self):
        return get_stock_rankings_by_return(self)
  
    def buy_stocks(self, ticker, shares):
        return buy_stock(self, ticker, shares)
    def sell_stocks(self, ticker, shares):
        return sell_stock(self, ticker, shares)
    def undo_last_trans(self):
        return undo_last_transaction(self)
    def redo_last_trans(self):
        return redo_last_transaction(self)
    def update_graph_with_corr(self, show_all=False):
        return update_graph_with_correlations(self, show_all=False)
    def get_networkx_gr(self):
        return get_networkx_graph(self)
    def monte_carlo_a(self, days=30):
        return monte_carlo_all(self, days=30)
    def merge_sort_st(self,stocks, key_index=1):
        return merge_sort_stocks(stocks, key_index)
    