import requests

API_KEY = "9a81248f7cc1e3dab938a678"
API_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair"

def convert_currency(from_currency, to_currency, amount):
    url = f"{API_URL}/{from_currency.upper()}/{to_currency.upper()}/{amount}"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if data['result'] != 'success':
            print("❌ API error:", data.get("error-type"))
            return None

        return data["conversion_result"]

    except requests.RequestException as e:
        print(f"❌ Network error: {e}")
        return None

def main():
    print("💱 Currency Converter (via exchangerate-api.com)")
    from_curr = input("From currency (e.g. USD): ").strip()
    to_curr = input("To currency (e.g. INR): ").strip()

    try:
        amount = float(input(f"Amount in {from_curr.upper()}: "))
    except ValueError:
        print("❌ Invalid amount.")
        return

    result = convert_currency(from_curr, to_curr, amount)
    if result:
        print(f"✅ {amount:.2f} {from_curr.upper()} = {result:.2f} {to_curr.upper()}")
    else:
        print("❌ Failed to convert.")

if __name__ == "__main__":
    main()
