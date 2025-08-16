from datastructures import HashTable
from portfolio_folder.portfolio_core import Portfolio
import hashlib
import streamlit as st

if "users" not in st.session_state:
    st.session_state["users"] = HashTable()

users = HashTable()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(email, password, initial_cash=10000.0):
    if users.get(email):
        return False, "User already exists"
    users.set(email, {
        "password_hash": hash_password(password),
        "portfolio": Portfolio(initial_cash=initial_cash)
    })
    return True, "Registration successful"

def login(email, password):
    user_data = users.get(email)
    if not user_data:
        return False, "Email not found"
    if user_data["password_hash"] != hash_password(password):
        return False, "Password does not match"
    st.session_state["current_user"] = email
    return True, f"Welcome {email}!"

def logout():
    if "current_user" in st.session_state:
        del st.session_state["current_user"]
    return True, "Logged out successfully"

def get_current_portfolio():
    email = st.session_state.get("current_user")
    if not email:
        return None
    user_data = users.get(email)
    return user_data["portfolio"] if user_data else None
