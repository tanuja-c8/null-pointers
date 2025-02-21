import streamlit as st
import sqlite3
import bcrypt

# Database Connection
conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

# Create users table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT UNIQUE,
                    password TEXT)''')
conn.commit()

# Function to hash passwords
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

# Function to verify passwords
def check_password(stored_password, entered_password):
    return bcrypt.checkpw(entered_password.encode(), stored_password.encode())

# Function to authenticate user
def authenticate(email, password):
    cursor.execute("SELECT password FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    if user and check_password(user[0], password):
        return True
    return False

# Login Function
def login():
    st.subheader("Login to Your Account")
    
    email = st.text_input("Enter your email")
    password = st.text_input("Enter your password", type="password")

    if st.button("Login"):
        if authenticate(email, password):
            st.session_state["logged_in"] = True
            st.session_state["email"] = email
            st.success("Login successful! Redirecting...")
            st.rerun()
        else:
            st.error("Invalid email or password.")

# Main function
def main():
    st.set_page_config(page_title="Study Planner", page_icon="📚", layout="centered")

    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    menu = ["Login", "Sign Up"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Login":
        if st.session_state["logged_in"]:
            st.switch_page("pages/chatbot.py")  # Redirect to Dashboard if already logged in
        else:
            login()
    elif choice == "Sign Up":
        st.switch_page("pages/signup.py")  # Redirect to Signup Page

if __name__ == "__main__":
    main()