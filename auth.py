from datastructures import HashTable  # Custom hash table implementation
from portfolio_folder.portfolio_core import Portfolio  # Portfolio class
import hashlib  # For password hashing
import streamlit as st  # Streamlit for UI and session state

if "users" not in st.session_state:#initialize users table in session state if not already present
    st.session_state["users"] = HashTable()

users = HashTable()#local users table 

def hash_password(password):#hash a password using SHA-256
    return hashlib.sha256(password.encode()).hexdigest()

def register(email, password, initial_cash=10000.0):#register a new user with email, password, and initial cash
    if users.get(email):  #check if user already exists
        return False, "User already exists"
    users.set(email, {   #store password hash and create a Portfolio
        "password_hash": hash_password(password),
        "portfolio": Portfolio(initial_cash=initial_cash)
    })
    return True, "Registration successful"

def login(email, password):#log in a user by checking email and password
    user_data = users.get(email)
    if not user_data:  # Email not found
        return False, "Email not found"
    if user_data["password_hash"] != hash_password(password):  #password mismatch
        return False, "Password does not match"
    st.session_state["current_user"] = email  #store current user in session
    return True, f"Welcome {email}!"

def logout():#log out the current user
    if "current_user" in st.session_state:
        del st.session_state["current_user"]
    return True, "Logged out successfully"
    
def get_current_portfolio():#retrieve the current user's Portfolio object
    email = st.session_state.get("current_user")
    if not email:
        return None
    user_data = users.get(email)
    return user_data["portfolio"] if user_data else None

