import json
import os

CONFIG_FILE = "user_settings.json"

# Default settings if config doesn't exist
DEFAULT_SETTINGS = {
    "dark_mode": False,
    "language": "en",
    "notifications": True
}

def load_settings():
    if not os.path.exists(CONFIG_FILE):
        print("⚠️ Config file not found. Loading default settings.")
        return DEFAULT_SETTINGS.copy()
    
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("❌ Error: Config file is corrupted. Loading defaults.")
        return DEFAULT_SETTINGS.copy()
    except Exception as e:
        print(f"❌ Error loading settings: {e}")
        return DEFAULT_SETTINGS.copy()

def save_settings(settings):
    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(settings, f, indent=4)
        print("✅ Settings saved successfully.")
    except Exception as e:
        print(f"❌ Error saving settings: {e}")

def update_setting(settings, key, value):
    if key not in settings:
        print(f"❌ '{key}' is not a valid setting.")
        return
    settings[key] = value
    print(f"✅ Updated '{key}' to '{value}'.")

def display_settings(settings):
    print("\n🔧 Current Settings:")
    for k, v in settings.items():
        print(f"  {k}: {v}")
    print()

def menu():
    settings = load_settings()
    
    while True:
        display_settings(settings)
        print("1. Toggle Dark Mode")
        print("2. Change Language")
        print("3. Toggle Notifications")
        print("4. Save and Exit")
        print("5. Exit Without Saving")

        choice = input("Choose an option (1–5): ").strip()

        if choice == "1":
            settings["dark_mode"] = not settings["dark_mode"]
            print(f"Dark Mode set to {settings['dark_mode']}")
        elif choice == "2":
            lang = input("Enter language code (e.g., en, fr, es): ").strip().lower()
            if lang:
                settings["language"] = lang
        elif choice == "3":
            settings["notifications"] = not settings["notifications"]
            print(f"Notifications set to {settings['notifications']}")
        elif choice == "4":
            save_settings(settings)
            break
        elif choice == "5":
            print("Exiting without saving.")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
