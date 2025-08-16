import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx
def monte_carlo_graph(portfolio):   
    st.subheader("Monte Carlo")  #monte carlo simulation section
    mc_days = st.slider("Days", 5, 60, 30)
    show_all_stocks = st.checkbox("Show all stocks in correlation graph and price paths", value=False)

    if st.button("Run Simulation"):
        portfolio.monte_carlo_a(days=mc_days)  #run monte carlo on all stocks
        #st.session_state.simulation_ran = True
        #st.rerun()
        if show_all_stocks:
            simulated_stocks = []
            for bucket in portfolio.simulated_returns.table:
                for ticker, returns in bucket:
                    simulated_stocks.append(ticker)
        else:
            simulated_stocks = []
            for bucket in portfolio.positions.table:
                for ticker, shares in bucket:
                    if shares > 0:
                        simulated_stocks.append(ticker)

        st.subheader("Monte Carlo Simulation Price Paths")  #plot Monte Carlo simulation price paths
        plt.figure(figsize=(10, 6))
        any_plotted = False
        for ticker in simulated_stocks:
            stock_data = portfolio.stocks.get(ticker)
            if not stock_data or not isinstance(stock_data, dict):
                continue
            prices = [stock_data.get('last_close', 0)]
            returns = portfolio.simulated_returns.get(ticker)
            if returns:
                for r in returns:
                    prices.append(prices[-1] * (1 + r))
                plt.plot(prices, label=ticker)
                any_plotted = True
        plt.xlabel("Days")
        plt.ylabel("Simulated Price")
        if any_plotted:
            plt.legend()
        st.pyplot(plt)
        plt.clf()
        portfolio.update_graph_with_corr() #update and show correlation graph
        G_nx = portfolio.get_networkx_gr()
        st.subheader("Correlation Graph")
        pos = nx.spring_layout(G_nx, seed=42)  #consistent layout
        edge_labels = nx.get_edge_attributes(G_nx, 'weight')
        edge_labels = {k: f"{v:.2f}" for k, v in edge_labels.items()}  #round edge weights for nicer labels

        plt.figure(figsize=(8, 6))
        nx.draw(G_nx, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=12, font_weight='bold')
        nx.draw_networkx_edge_labels(G_nx, pos, edge_labels=edge_labels, font_color='red')
        st.pyplot(plt)
        plt.clf()
    else:
        st.info("Click 'Run Simulation' to run Monte Carlo on all stocks")