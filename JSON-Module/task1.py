import json
import os
from pathlib import Path

def resolve_json_path(user_input):
    # Map common folder keywords to full paths
    known = {
        "desktop": Path.home() / "Desktop" / "resume.json",
        "downloads": Path.home() / "Downloads" / "resume.json",
        "documents": Path.home() / "Documents" / "resume.json"
    }
    key = user_input.strip().lower()
    return known.get(key, Path(user_input).expanduser().resolve())

def validate_json_file(path):
    if not os.path.exists(path):
        print("❌ Error: File does not exist.")
        return False
    if not str(path).lower().endswith(".json"):
        print("❌ Error: Not a .json file.")
        return False
    return True

def load_resume(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON format: {e}")
        return None
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return None

def print_section(title, content):
    print(f"\n🔹 {title}")
    print('-' * (len(title) + 3))
    if isinstance(content, list):
        for item in content:
            if isinstance(item, dict):
                for k, v in item.items():
                    print(f"{k.capitalize()}: {v}")
                print()
            else:
                print(f"- {item}")
    elif isinstance(content, dict):
        for k, v in content.items():
            print(f"{k.capitalize()}: {v}")
    else:
        print(content)

def display_resume(data):
    if not isinstance(data, dict):
        print("❌ Resume data is not in expected format.")
        return

    print("\n📄 === RESUME ===\n")

    basic_fields = ['name', 'email', 'phone', 'address', 'summary']
    for field in basic_fields:
        if field in data:
            print(f"{field.capitalize()}: {data[field]}")

    for section in ['education', 'experience', 'skills', 'projects', 'certifications']:
        if section in data:
            print_section(section.capitalize(), data[section])

if __name__ == "__main__":
    file_input = input("Enter path to JSON resume file (or 'desktop', 'downloads'): ").strip()
    abs_path = resolve_json_path(file_input)

    if validate_json_file(abs_path):
        resume_data = load_resume(abs_path)
        if resume_data:
            display_resume(resume_data)
