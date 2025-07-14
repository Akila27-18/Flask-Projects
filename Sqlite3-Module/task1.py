import sqlite3
import datetime

DB_NAME = "notes.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_note():
    title = input("Title: ").strip()
    content = input("Content:\n").strip()
    if not title or not content:
        print("❌ Title and content are required.")
        return

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (title, content, created_at) VALUES (?, ?, ?)",
                   (title, content, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()
    print("✅ Note added.")

def view_notes():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, created_at FROM notes ORDER BY created_at DESC")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("⚠️ No notes found.")
        return

    print("\n📋 Your Notes:")
    for row in rows:
        print(f"[{row[0]}] {row[1]} ({row[2]})")

def read_note():
    note_id = input("Enter Note ID to view: ").strip()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
    note = cursor.fetchone()
    conn.close()

    if note:
        print(f"\n📝 {note[1]} ({note[3]})\n{'-'*40}\n{note[2]}\n")
    else:
        print("❌ Note not found.")

def update_note():
    note_id = input("Enter Note ID to update: ").strip()
    new_title = input("New Title: ").strip()
    new_content = input("New Content:\n").strip()

    if not new_title or not new_content:
        print("❌ Title and content cannot be empty.")
        return

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE notes SET title = ?, content = ? WHERE id = ?",
                   (new_title, new_content, note_id))
    if cursor.rowcount == 0:
        print("❌ Note not found.")
    else:
        print("✅ Note updated.")
    conn.commit()
    conn.close()

def delete_note():
    note_id = input("Enter Note ID to delete: ").strip()
    confirm = input(f"Are you sure you want to delete note {note_id}? (y/n): ").lower()
    if confirm != 'y':
        return

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    if cursor.rowcount == 0:
        print("❌ Note not found.")
    else:
        print("🗑️ Note deleted.")
    conn.commit()
    conn.close()

def main():
    init_db()
    while True:
        print("\n📓 Simple Notes App")
        print("1. Add Note")
        print("2. View All Notes")
        print("3. Read Note by ID")
        print("4. Update Note")
        print("5. Delete Note")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()
        if choice == '1':
            add_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            read_note()
        elif choice == '4':
            update_note()
        elif choice == '5':
            delete_note()
        elif choice == '6':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
