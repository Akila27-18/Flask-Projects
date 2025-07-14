import os
from pathlib import Path

def validate_directory(path):
    if not os.path.exists(path):
        print("❌ Error: Path does not exist.")
        return False
    if not os.path.isdir(path):
        print("❌ Error: Not a directory.")
        return False
    if not os.access(path, os.R_OK):
        print("❌ Error: Directory is not readable.")
        return False
    return True

def resolve_path(user_input):
    # Handle known Windows folders like desktop, downloads, etc.
    special = {
        "desktop": os.path.join(Path.home(), "Desktop"),
        "downloads": os.path.join(Path.home(), "Downloads"),
        "documents": os.path.join(Path.home(), "Documents"),
        "pictures": os.path.join(Path.home(), "Pictures"),
        "videos": os.path.join(Path.home(), "Videos")
    }
    key = user_input.strip().lower()
    return special.get(key, os.path.abspath(user_input))

def search_files(base_path, keyword):
    print(f"\n🔍 Searching for '{keyword}' in: {base_path}\n")
    matches = []

    for root, dirs, files in os.walk(base_path):
        for filename in files:
            if keyword.lower() in filename.lower():
                full_path = os.path.join(root, filename)
                matches.append(full_path)

    if matches:
        print(f"✅ Found {len(matches)} matching files:\n")
        for match in matches:
            print(match)
    else:
        print("❌ No matching files found.")

if __name__ == "__main__":
    folder_input = input("Enter folder path to search in (or 'desktop', 'downloads', etc.): ").strip()
    keyword_input = input("Enter full or partial filename (e.g., 'report', '.pdf', 'image.jpg'): ").strip()

    search_path = resolve_path(folder_input)

    if validate_directory(search_path):
        if keyword_input:
            search_files(search_path, keyword_input)
        else:
            print("❌ Error: Search keyword cannot be empty.")
