import streamlit as st
import matplotlib.pyplot as plt
def display_portfolio_(portfolio):
    st.subheader(" Current Portfolio")
    portfolio_data, total_value = portfolio.show_port()
    for line in portfolio_data:
        st.write(line)
    st.write(f"**Total Stock Value:** ${total_value:,.2f}")
    st.write(f"**Total Portfolio Value (Stocks + Cash):** ${total_value + portfolio.cash:,.2f}")
    labels = []
    sizes = []
    for bucket in portfolio.positions.table:
        for ticker, shares in bucket:
            if shares > 0:
                stock_data = portfolio.stocks.get(ticker)
                price = stock_data.get('last_close', 0) if stock_data else 0
                labels.append(ticker)
                sizes.append(shares * price)
 # Add cash as a slice
    if portfolio.cash > 0:
        labels.append("Cash")
        sizes.append(portfolio.cash)

    if sizes:  # only plot if there’s at least one item
        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title("Portfolio Allocation")
        st.pyplot(plt)
        plt.clf()
    else:
        st.write("No assets to display in pie chart.")
   