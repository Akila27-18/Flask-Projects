import json
import os

TODO_FILE = "todo_data.json"

# Load tasks from JSON file or return empty list
def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    try:
        with open(TODO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("⚠️ Warning: Corrupted todo file. Starting fresh.")
        return []
    except Exception as e:
        print(f"❌ Error loading tasks: {e}")
        return []

# Save tasks to JSON file
def save_tasks(tasks):
    try:
        with open(TODO_FILE, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=4)
    except Exception as e:
        print(f"❌ Error saving tasks: {e}")

# Display all tasks
def list_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks found.")
        return
    print("\n📋 Todo List:")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {status} {task['task']}")

# Add new task
def add_task(tasks):
    task_text = input("Enter new task: ").strip()
    if task_text:
        tasks.append({"task": task_text, "done": False})
        print("✅ Task added.")
    else:
        print("❌ Task cannot be empty.")

# Mark task as done
def mark_done(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]["done"] = True
            print("✅ Task marked as done.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Delete task
def delete_task(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"🗑️ Deleted: {removed['task']}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Menu loop
def main():
    tasks = load_tasks()
    while True:
        print("\n--- Todo Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Save and Exit")

        choice = input("Choose an option (1–5): ").strip()

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("💾 Changes saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
