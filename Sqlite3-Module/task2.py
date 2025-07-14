import sqlite3
import hashlib
import getpass

DB_NAME = "users.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    print("\n📝 Register New User")
    username = input("Username: ").strip()
    password = getpass.getpass("Password: ")
    confirm = getpass.getpass("Confirm Password: ")

    if password != confirm:
        print("❌ Passwords do not match.")
        return

    if len(password) < 6:
        print("❌ Password must be at least 6 characters.")
        return

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
                    (username, hash_password(password)))
        conn.commit()
        print("✅ User registered successfully.")
    except sqlite3.IntegrityError:
        print("❌ Username already exists.")
    conn.close()

def login():
    print("\n🔐 User Login")
    username = input("Username: ").strip()
    password = getpass.getpass("Password: ")

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    row = cur.fetchone()
    conn.close()

    if row and row[0] == hash_password(password):
        print(f"✅ Login successful! Welcome, {username}.")
    else:
        print("❌ Invalid username or password.")

def main():
    init_db()
    while True:
        print("\n🔒 User Login System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
