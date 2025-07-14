import re
import os

# Regular expression pattern to match emails
EMAIL_REGEX = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

def extract_emails(file_path):
    if not os.path.exists(file_path):
        print("❌ Error: File does not exist.")
        return []

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Find all emails
    emails = re.findall(EMAIL_REGEX, content)
    return sorted(set(emails))  # remove duplicates and sort

def main():
    print("📧 Email Extractor from Text File")
    path = input("Enter path to text file: ").strip()

    emails = extract_emails(path)
    if emails:
        print(f"\n✅ Found {len(emails)} email(s):")
        for email in emails:
            print(" -", email)
        
        # Optional: Save to file
        save = input("\nDo you want to save the results to 'emails.txt'? (y/n): ").strip().lower()
        if save == 'y':
            with open("emails.txt", "w") as f:
                for email in emails:
                    f.write(email + "\n")
            print("💾 Saved to 'emails.txt'")
    else:
        print("⚠️ No email addresses found.")

if __name__ == "__main__":
    main()
