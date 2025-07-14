import os
from pathlib import Path

def get_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            try:
                fp = os.path.join(dirpath, f)
                if os.path.exists(fp):
                    total_size += os.stat(fp).st_size
            except Exception as e:
                print(f"⚠️ Error reading {fp}: {e}")
    return total_size

def sizeof_fmt(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024:
            return f"{num:.2f}{unit}{suffix}"
        num /= 1024
    return f"{num:.2f}Y{suffix}"

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

# Handle known Windows folders
def resolve_path(user_input):
    special = {
        "desktop": os.path.join(Path.home(), "Desktop"),
        "downloads": os.path.join(Path.home(), "Downloads"),
        "documents": os.path.join(Path.home(), "Documents"),
        "pictures": os.path.join(Path.home(), "Pictures"),
        "videos": os.path.join(Path.home(), "Videos")
    }
    key = user_input.strip().lower()
    return special.get(key, os.path.abspath(user_input))

def analyze_directory_usage(base_path):
    folder_sizes = {}
    for root, dirs, files in os.walk(base_path):
        folder_size = 0
        for name in files:
            try:
                filepath = os.path.join(root, name)
                if os.path.isfile(filepath):
                    folder_size += os.stat(filepath).st_size
            except Exception as e:
                print(f"⚠️ Error with {filepath}: {e}")
        folder_sizes[root] = folder_size

    print("\n📊 Disk Usage per Folder:\n")
    for folder in sorted(folder_sizes, key=folder_sizes.get, reverse=True):
        print(f"{sizeof_fmt(folder_sizes[folder]):>10}  |  {folder}")

if __name__ == "__main__":
    user_input = input("Enter the path to analyze (or 'desktop', 'downloads'): ").strip()
    path = resolve_path(user_input)

    if validate_directory(path):
        analyze_directory_usage(path)
