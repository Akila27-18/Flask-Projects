import os
import shutil
from pathlib import Path

# Known Windows special folders
KNOWN_FOLDERS = {
    'downloads': os.path.join(Path.home(), 'Downloads'),
    'desktop': os.path.join(Path.home(), 'Desktop'),
    'documents': os.path.join(Path.home(), 'Documents'),
    'pictures': os.path.join(Path.home(), 'Pictures'),
    'videos': os.path.join(Path.home(), 'Videos'),
}

EXTENSION_MAP = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.odt'],
    'Spreadsheets': ['.xls', '.xlsx', '.csv'],
    'Presentations': ['.ppt', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Video': ['.mp4', '.avi', '.mov', '.mkv'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.html', '.css', '.php', '.sh', '.bat'],
    'Executables': ['.exe', '.msi', '.apk'],
    'Others': []
}

def get_folder_for_extension(ext):
    ext = ext.lower()
    for folder, extensions in EXTENSION_MAP.items():
        if ext in extensions:
            return folder
    return 'Others'

def validate_directory(path):
    if not os.path.exists(path):
        print("❌ Error: Directory does not exist.")
        return False
    if not os.path.isdir(path):
        print("❌ Error: Provided path is not a directory.")
        return False
    if not os.access(path, os.R_OK | os.W_OK):
        print("❌ Error: No read/write access to the directory.")
        return False
    return True

def resolve_path(user_input):
    key = user_input.strip().lower()
    if key in KNOWN_FOLDERS:
        return KNOWN_FOLDERS[key]
    return os.path.abspath(user_input)

def organize_directory(path):
    if not validate_directory(path):
        return

    files = os.listdir(path)

    for file in files:
        full_path = os.path.join(path, file)
        if not os.path.isfile(full_path) or file.startswith('.'):
            continue

        _, ext = os.path.splitext(file)
        folder = get_folder_for_extension(ext)
        folder_path = os.path.join(path, folder)

        os.makedirs(folder_path, exist_ok=True)

        dest_path = os.path.join(folder_path, file)

        if os.path.exists(dest_path):
            base, extension = os.path.splitext(file)
            counter = 1
            while True:
                new_name = f"{base}_{counter}{extension}"
                dest_path = os.path.join(folder_path, new_name)
                if not os.path.exists(dest_path):
                    break
                counter += 1

        try:
            shutil.move(full_path, dest_path)
            print(f"✅ Moved: {file} → {folder}/")
        except Exception as e:
            print(f"⚠️ Error moving {file}: {e}")

    print("✔️ Organization complete.")

if __name__ == "__main__":
    user_input = input("Enter path (or folder name like 'downloads'): ").strip()
    user_path = resolve_path(user_input)
    organize_directory(user_path)
