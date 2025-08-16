import streamlit as st
import pandas as pd
def portfolio_graphs(portfolio):
    st.subheader("Portfolio Value Over Time")
    change_info = portfolio.get_portfolio_chan()  #portfolio change display
    if isinstance(change_info, dict):
        cols = st.columns(len(change_info))
        for col, (key, value) in zip(cols, change_info.items()):
            with col:
                st.markdown(f"**{key}:**")
                st.write(value)
    else:
        st.write(change_info)

    values = portfolio.get_portfolio_val()  #value progression
    if len(values) > 1:
        df = pd.DataFrame({"Portfolio Value": values})
        st.line_chart(df)
    elif len(values) == 1:
        st.write(f"Current Portfolio Value: ${values[0]:,.2f}")