from werkzeug.security import generate_password_hash, check_password_hash

def hash_password():
    password = input("🔑 Enter password to hash: ").strip()
    if not password:
        print("❌ Password cannot be empty.")
        return None

    valid_methods = ["pbkdf2:sha256", "pbkdf2:sha1", "sha256", "md5"]
    hash_method = input("Choose hash method (default: pbkdf2:sha256): ").strip() or "pbkdf2:sha256"

    if hash_method not in valid_methods:
        print("❌ Invalid method. Using default: pbkdf2:sha256")
        hash_method = "pbkdf2:sha256"

    hashed = generate_password_hash(password, method=hash_method)
    print(f"\n🔐 Hashed password:\n{hashed}")
    return hashed

def verify_password(stored_hash):
    attempt = input("\n🔁 Re-enter password to verify: ").strip()
    if check_password_hash(stored_hash, attempt):
        print("✅ Password verified successfully.")
    else:
        print("❌ Password does not match.")

def main():
    print("🔐 Password Hashing Tool")
    hashed_pw = hash_password()
    if hashed_pw:
        verify_password(hashed_pw)

if __name__ == "__main__":
    main()
