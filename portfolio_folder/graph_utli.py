from datastructures import HashTable
import networkx as nx
import numpy as np
def update_graph_with_correlations(self, show_all=False):
        held_tickers = [] #Collect only stocks with shares held > 0
        for bucket in self.positions.table:
            for ticker, shares in bucket:
                if shares > 0:
                    held_tickers.append(ticker)
        filtered_returns = HashTable()
        for bucket in self.simulated_returns.table:
            for ticker, returns in bucket:
                if ticker in held_tickers and len(returns) > 1:
                    filtered_returns.set(ticker, returns)
        self.stock_network.clear()  #clear all vertices and edges
        for ticker in held_tickers:#add only held tickers as vertices
            self.stock_network.add_vertex(ticker)

        tickers = filtered_returns.keys()
        for i in range(len(tickers)):
            for j in range(i + 1, len(tickers)):
                t1, t2 = tickers[i], tickers[j]
                r1 = np.array(filtered_returns.get(t1))
                r2 = np.array(filtered_returns.get(t2))
                corr = np.corrcoef(r1, r2)[0,1]
                if not np.isnan(corr):
                    self.stock_network.add_edge(t1, t2, weight=corr)


def get_networkx_graph(self): #convert Graph data structure into a NetworkX graph
        G = nx.Graph()
        for v in self.stock_network.vertices():
            G.add_node(v)
        for v in self.stock_network.vertices():
            for neighbor, weight in self.stock_network.get_neighbors(v):  #adjust Graph's edge
                G.add_edge(v, neighbor, weight=weight)
        return G