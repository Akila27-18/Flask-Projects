import json
from werkzeug.datastructures import CallbackDict

SESSION_FILE = "session.json"

def save_session(session):
    with open(SESSION_FILE, "w", encoding="utf-8") as f:
        json.dump(dict(session), f)

def load_session():
    try:
        with open(SESSION_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    return CallbackDict(data, on_update=save_session)

def login(session):
    username = input("👤 Enter your username: ").strip()
    session["username"] = username
    print(f"✅ Logged in as {username}")

def view_session(session):
    if "username" in session:
        print(f"👤 Current user: {session['username']}")
    else:
        print("❌ No user logged in.")

def logout(session):
    session.clear()
    print("👋 Logged out and session cleared.")

def main():
    print("🔐 CLI Session Manager (Like Flask Sessions)")
    session = load_session()

    while True:
        print("\n1. Login\n2. View Session\n3. Logout\n4. Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            login(session)
        elif choice == "2":
            view_session(session)
        elif choice == "3":
            logout(session)
        elif choice == "4":
            print("🔒 Exiting...")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
