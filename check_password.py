import sqlite3
import bcrypt

# Connect to SQLite database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# 🔹 Replace these with your actual test credentials
email = "test@example.com"   # Enter the email you used in signup
password = "yourpassword"     # Enter the password you used in signup

# Fetch stored password for the given email
cursor.execute("SELECT password FROM users WHERE email = ?", (email,))
row = cursor.fetchone()

if row:
    stored_password = row[0]  # Get the hashed password from DB

    # Verify password using bcrypt
    if bcrypt.checkpw(password.encode(), stored_password.encode()):
        print("✅ Login Successful! Password matches.")
    else:
        print("❌ Incorrect Password!")
else:
    print("❌ Email Not Found!")

conn.close()
