import sqlite3
import csv
import os

def init_db():
    conn = sqlite3.connect("users_safe.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS users")
    c.execute("CREATE TABLE users (username TEXT, password TEXT)")
    c.execute("INSERT INTO users VALUES ('admin', 'secret')")
    conn.commit()
    conn.close()

def login(username, password):
    conn = sqlite3.connect("users_safe.db")
    c = conn.cursor()
    # SAFE: Parameterized query prevents injection
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    c.execute(query, (username, password))
    result = c.fetchone()
    conn.close()
    log_attempt(username, password, "success" if result else "fail")
    return result is not None

def log_attempt(username, password, status):
    with open("login_attempts_safe.csv", "a", newline="") as f:
        writer = csv.writer(f)
        if os.path.getsize("login_attempts_safe.csv") == 0:
            writer.writerow(["username", "password", "status"])
        writer.writerow([username, password, status])

if __name__ == "__main__":
    init_db()
    print("Normal login test:")
    print("admin/secret:", login("admin", "secret"))
    print("admin/wrong:", login("admin", "wrong"))
    print("\nSQL injection test:")
    exploit = "' OR '1'='1"
    print(f"admin/{exploit}:", login("admin", exploit))  # Should fail now!


