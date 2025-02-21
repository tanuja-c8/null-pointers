import streamlit as st
import sqlite3
import bcrypt

# Database Connection
conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

# Function to hash passwords
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

# Function to register new users
def register():
    st.subheader("Create an Account")

    new_email = st.text_input("Enter your email")
    new_password = st.text_input("Enter your password", type="password")

    if st.button("Sign Up"):
        if new_email and new_password:
            hashed_password = hash_password(new_password)
            try:
                cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (new_email, hashed_password))
                conn.commit()
                st.success("Account created successfully! Please log in.")
                st.switch_page("app.py")  # Redirect to Login
            except sqlite3.IntegrityError:
                st.error("Email already exists. Try logging in.")
        else:
            st.warning("Please enter both email and password.")

if __name__ == "__main__":
    register()
