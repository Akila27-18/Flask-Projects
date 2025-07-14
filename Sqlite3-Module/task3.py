import sqlite3

DB_NAME = "students.db"
SUBJECTS = ["Math", "Science", "English"]

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            math INTEGER NOT NULL,
            science INTEGER NOT NULL,
            english INTEGER NOT NULL,
            average REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_valid_mark(subject):
    while True:
        try:
            mark = int(input(f"Enter marks for {subject} (0–100): "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("❌ Must be between 0 and 100.")
        except ValueError:
            print("❌ Please enter a valid number.")

def add_student():
    name = input("Enter student name: ").strip()
    if not name:
        print("❌ Name cannot be empty.")
        return

    marks = {}
    for subject in SUBJECTS:
        marks[subject] = get_valid_mark(subject)

    avg = sum(marks.values()) / len(SUBJECTS)

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO students (name, math, science, english, average)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, marks["Math"], marks["Science"], marks["English"], avg))
    conn.commit()
    conn.close()
    print("✅ Student added successfully.")

def view_students():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT name, math, science, english, average FROM students")
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("⚠️ No students found.")
        return

    print("\n📊 Student Marks:")
    print("-" * 60)
    print(f"{'Name':<15} {'Math':<7} {'Science':<8} {'English':<8} {'Average':<7}")
    print("-" * 60)
    for row in rows:
        print(f"{row[0]:<15} {row[1]:<7} {row[2]:<8} {row[3]:<8} {row[4]:<7.2f}")
    print("-" * 60)

def main():
    init_db()
    while True:
        print("\n📘 Student Mark Tracker")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
