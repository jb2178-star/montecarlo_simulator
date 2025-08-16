import streamlit as st
from auth import register, login, logout, get_current_portfolio
from ui_folder.ui import run_ui

def login_ui_():
    if "current_user" not in st.session_state:
        st.session_state["current_user"] = None

    # --- User is logged in ---
    if st.session_state["current_user"] is not None:
        st.subheader(f"Welcome, {st.session_state.current_user}")
        portfolio = get_current_portfolio()
        if portfolio:
            run_ui()

        if st.button("Logout"):
            logout()
            st.rerun()  # immediately go back to login page
        return  # stop executing rest of the function

    # --- User is NOT logged in ---
    st.title("Portfolio App Login")
    tab = st.radio("Select action", ["Login", "Register"])

    if tab == "Register":
        st.subheader("Create a new account")
        reg_email = st.text_input("Email", key="reg_email")
        reg_password = st.text_input("Password", type="password", key="reg_password")
        reg_cash = st.number_input("Initial cash ($)", value=10000.0, step=100.0)

        if st.button("Register", key="register_btn"):
            success, message = register(reg_email, reg_password, reg_cash)
            if success:
                st.success(message)
            else:
                st.error(message)

    elif tab == "Login":
        st.subheader("Login to your account")
        login_email = st.text_input("Email", key="login_email")
        login_password = st.text_input("Password", type="password", key="login_password")

        if st.button("Login", key="login_btn"):
            success, message = login(login_email, login_password)
            if success:
                st.success(message)
                st.rerun()  # immediately go to main UI
            else:
                st.error(message)

    
