import streamlit as st
def sorting_uis(portfolio):
    col1, col2, col3 = st.columns(3)  #show stocks alphabetically or price
    with col1:
        if "show_alpha" not in st.session_state:
            st.session_state.show_alpha = False

        if st.button("Show Stocks Alphabetically"):
            st.session_state.show_alpha = not st.session_state.show_alpha

        if st.session_state.show_alpha:
            sorted_stocks = portfolio.get_stock_rank()

            search_term = st.text_input("Search ticker (A-Z):").strip().upper()
            filtered_stocks = [(t, p) for t, p in sorted_stocks if search_term in t] if search_term else sorted_stocks

            page_size = 5
            num_pages = (len(filtered_stocks) + page_size - 1) // page_size
            page = st.number_input(
                f"Page (1-{num_pages}):",
                min_value=1,
                max_value=max(num_pages, 1),
                step=1,
                key="page_alpha"  #unique key added here
            )

            start_idx = (page - 1) * page_size
            end_idx = start_idx + page_size
            page_stocks = filtered_stocks[start_idx:end_idx]

            st.write(f"**Stocks (A-Z), showing {len(page_stocks)} of {len(filtered_stocks)} matching**")
            for ticker, price in page_stocks:
                st.write(f"{ticker}: ${price:.2f}")

    with col2:
        if "show_price" not in st.session_state:
            st.session_state.show_price = False

        if st.button("Show Stocks by Price"):
            st.session_state.show_price = not st.session_state.show_price

        if st.session_state.show_price:
            sorted_stocks = portfolio.get_stock_rank()
            price_sorted=portfolio.merge_sort_st(sorted_stocks, key_index=1)

            search_term_price = st.text_input("Search ticker (Price):").strip().upper()
            filtered_price_stocks = [(t, p) for t, p in price_sorted if search_term_price in t] if search_term_price else price_sorted

            page_size = 5
            num_pages_price = (len(filtered_price_stocks) + page_size - 1) // page_size
            page_price = st.number_input(
                f"Page (1-{num_pages_price}):",
                min_value=1,
                max_value=max(num_pages_price, 1),
                step=1,
                key="page_price"  #unique key added here
            )

            start_idx_price = (page_price - 1) * page_size
            end_idx_price = start_idx_price + page_size
            page_price_stocks = filtered_price_stocks[start_idx_price:end_idx_price]

            st.write(f"**Stocks by Price (High to Low), showing {len(page_price_stocks)} of {len(filtered_price_stocks)} matching**")
            for ticker, price in page_price_stocks:
                st.write(f"{ticker}: ${price:.2f}")
    with col3:
        if "show_return" not in st.session_state:
            st.session_state.show_return = False

        if st.button("Show Stocks by Return"):
            st.session_state.show_return = not st.session_state.show_return

        if st.session_state.show_return:
            sorted_returns = portfolio.get_stock_rankings_by_ret()  # (ticker, cumulative_return)
            return_sorted=portfolio.merge_sort_st(sorted_returns, key_index=1)
            search_term_return = st.text_input("Search ticker (Return):").strip().upper()
            filtered_return_stocks = [(t, r) for t, r in return_sorted if search_term_return in t] if search_term_return else return_sorted

            page_size = 5
            num_pages_return = (len(filtered_return_stocks) + page_size - 1) // page_size
            page_return = st.number_input(
                f"Page (1-{num_pages_return}):",
                min_value=1,
                max_value=max(num_pages_return, 1),
                step=1,
                key="page_return"
            )

            start_idx_return = (page_return - 1) * page_size
            end_idx_return = start_idx_return + page_size
            page_return_stocks = filtered_return_stocks[start_idx_return:end_idx_return]

            st.write(f"**Stocks by Return (High to Low), showing {len(page_return_stocks)} of {len(filtered_return_stocks)} matching**")
            for ticker, ret in page_return_stocks:
                st.write(f"{ticker}: {ret*100:.2f}%")
