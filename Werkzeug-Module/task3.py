from urllib.parse import urlencode

def build_url():
    base = input("🔗 Enter base URL (e.g., https://example.com/api): ").strip().rstrip('/')
    if not base:
        print("❌ Base URL is required.")
        return

    path = input("📁 Enter path (e.g., 'v1/users'): ").strip().lstrip('/')
    full_path = f"{base}/{path}" if path else base

    query_params = {}
    while True:
        add = input("➕ Add query param? (y/n): ").strip().lower()
        if add != 'y':
            break
        key = input("   Key: ").strip()
        value = input("   Value: ").strip()
        query_params[key] = value

    query_string = urlencode(query_params)
    final_url = f"{full_path}?{query_string}" if query_string else full_path

    print("\n🔧 Final Built URL:")
    print(final_url)

def main():
    print("🌐 URL Builder (No Werkzeug dependencies)")
    while True:
        build_url()
        again = input("\n🔁 Build another? (y/n): ").strip().lower()
        if again != 'y':
            break
    print("👋 Done!")

if __name__ == "__main__":
    main()
