import sqlite3
import csv
import os

# Setup SQLite DB
def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS users")
    c.execute("CREATE TABLE users (username TEXT, password TEXT)")
    c.execute("INSERT INTO users VALUES ('admin', 'secret')")
    c.execute("INSERT INTO users VALUES ('guest', 'pass123')")
    conn.commit()
    conn.close()
    print("Database initialized with users: admin/secret, guest/pass123")

# Vulnerable login function
def login(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    # DANGER: Raw string interpolation = SQL injection risk!
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    c.execute(query)
    result = c.fetchone()
    conn.close()
    log_attempt(username, password, "success" if result else "fail")
    return result is not None

# Log attempts to CSV (like log_list_v2.py)
def log_attempt(username, password, status):
    with open("login_attempts.csv", "a", newline="") as f:
        writer = csv.writer(f)
        if os.path.getsize("login_attempts.csv") == 0:
            writer.writerow(["username", "password", "status"])
        writer.writerow([username, password, status])

# Main execution
if __name__ == "__main__":
    init_db()
    
    # Test normal login
    print("Normal login test:")
    print("admin/secret:", login("admin", "secret"))  # Should succeed
    print("admin/wrong:", login("admin", "wrong"))   # Should fail
    
    # Test SQL injection
    print("\nSQL injection test:")
    # Exploit: ' OR '1'='1 bypasses password check
    exploit = "' OR '1'='1"
    print(f"admin/{exploit}:", login("admin", exploit))  # Should succeed!


