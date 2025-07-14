import re

def validate_password(password):
    errors = []

    if len(password) < 8:
        errors.append("❌ Must be at least 8 characters long.")
    if not re.search(r"[A-Z]", password):
        errors.append("❌ Must contain at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        errors.append("❌ Must contain at least one lowercase letter.")
    if not re.search(r"\d", password):
        errors.append("❌ Must contain at least one digit.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        errors.append("❌ Must contain at least one special character.")

    return errors

def main():
    print("🔐 Password Validator")
    password = input("Enter your password: ")

    errors = validate_password(password)
    if not errors:
        print("✅ Password is strong!")
    else:
        print("\n⚠️ Password is weak:")
        for err in errors:
            print(err)

if __name__ == "__main__":
    main()
