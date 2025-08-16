import streamlit as st
def transaction_uis(portfolio):
    st.subheader("Buy / Sell Stocks")  #selection buy/sell
    col1, col2, col3 = st.columns(3)
    with col1:
        action = st.selectbox("Action", ["BUY", "SELL"])
    with col2:
        tickers = portfolio.get_all_tickers()
        ticker = st.selectbox("Ticker", options=tickers)
        price_data = portfolio.stocks.get(ticker)
        price = price_data.get('last_close', 0) if price_data else 0
        st.write(f"Current Price for {ticker}: ${price:.2f}")
    with col3:
        shares = st.number_input("Shares", min_value=1, step=1, value=1)
        price_data = portfolio.stocks.get(ticker)
        if price_data and isinstance(price_data, dict):
            price = price_data.get('last_close', 0)
        else:
            price = 0
        share_price = price * shares
        st.write(f"Cost for {shares} share(s): ${share_price:.2f}")
    if st.button("Submit Transaction"):  #process buy/sell
        if ticker.strip():
            if action == "BUY":
                st.success(portfolio.buy_stocks(ticker, shares))
            else:
                st.success(portfolio.sell_stocks(ticker, shares))
        else:
            st.warning("Please enter a valid ticker.")

    col1, col2 = st.columns(2)  #undo/redo
    with col1:
        if st.button("Undo Last Transaction"):
            st.info(portfolio.undo_last_trans())
    with col2:
        if st.button("Redo Last Transaction"):
            st.info(portfolio.redo_last_trans())
    st.subheader(" Transaction History")
    history = portfolio.show_transaction_history()
    if history:
        for h in history[-5:][::-1]:
            st.write(h)
    else:
        st.write("No transactions yet.")