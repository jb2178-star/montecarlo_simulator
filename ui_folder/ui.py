import streamlit as st
import pandas as pd

from portfolio_folder.portfolio_core import Portfolio
from ui_folder.monte_carlo_ui import monte_carlo_graph
from ui_folder.transaction_ui import transaction_uis
from ui_folder.pca_ui import pca_uis
from ui_folder.list_ui import sorting_uis
from ui_folder.portfolio_graph_ui import portfolio_graphs
from ui_folder.display_portfolio_ui import display_portfolio_


def run_ui():
    st.title("Portfolio/Monte Carlo Simulation")
    if "portfolio" not in st.session_state:  #initialize portfolio in session state
        st.session_state.portfolio = Portfolio(initial_cash=10000.0)
    portfolio = st.session_state.portfolio
    new_cash = st.number_input("Set Cash Amount", min_value=0.0, value=portfolio.cash, step=100.0, format="%.2f")  # input to set cash
    if new_cash != portfolio.cash:
        portfolio.set_cash(new_cash)
        st.success(f"Cash: ${new_cash:.2f}")
    # Create tabs
    tabs = st.tabs([
        "Transactions",
        "Portfolio Display",
        "Sorting / Rankings",
        "Portfolio Value Over Time",
        "Monte Carlo / Correlations",
        "PCA Analysis"
    ])

    with tabs[0]:
        st.header("Transactions")
        transaction_uis(portfolio)

    with tabs[1]:
        st.header("Portfolio Overview")
        display_portfolio_(portfolio)

    with tabs[2]:
        st.header("Sorting / Rankings")
        sorting_uis(portfolio)

    with tabs[3]:
        st.header("Portfolio Value")
        portfolio_graphs(portfolio)

    with tabs[4]:
        st.header("Monte Carlo Simulation")
        monte_carlo_graph(portfolio)

    with tabs[5]:
        st.header("PCA Analysis")
        pca_uis(portfolio)
    
