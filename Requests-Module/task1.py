import requests

API_KEY = "fb603430fe4e84c0fc66998296ffecf5"  # 🔁 Replace with your real key
BASE_URL = "http://api.weatherstack.com/current"

def get_weather(city):
    params = {
        "access_key": API_KEY,
        "query": city
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        data = response.json()

        if "error" in data:
            print(f"❌ Error: {data['error']['info']}")
            return None
        return data

    except requests.RequestException as e:
        print(f"❌ Network error: {e}")
        return None

def display_weather(data):
    location = data["location"]["name"]
    country = data["location"]["country"]
    temperature = data["current"]["temperature"]
    desc = data["current"]["weather_descriptions"][0]
    humidity = data["current"]["humidity"]
    wind = data["current"]["wind_speed"]

    print(f"\n🌍 Weather in {location}, {country}")
    print(f"🔸 Condition : {desc}")
    print(f"🌡️ Temp      : {temperature}°C")
    print(f"💧 Humidity  : {humidity}%")
    print(f"🌬️ Wind Speed: {wind} km/h")

def main():
    print("☁️ Weather CLI App (Weatherstack)")
    
    if API_KEY == "your_api_key_here":
        print("❌ Please set your Weatherstack API key first.")
        return

    city = input("Enter city name: ").strip()
    if not city:
        print("❌ City name cannot be empty.")
        return

    data = get_weather(city)
    if data:
        display_weather(data)

if __name__ == "__main__":
    main()
