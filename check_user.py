import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Fetch all users
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

# Print the stored users
if users:
    print("✅ Users found in database:")
    for user in users:
        print(user)  # Should print (email, hashed_password)
else:
    print("❌ No users found! Signup might be failing.")

# Close the connection
conn.close()
