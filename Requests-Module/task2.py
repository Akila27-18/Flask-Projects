import requests

GITHUB_API = "https://api.github.com/users/"

def fetch_profile(username):
    url = GITHUB_API + username
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print("❌ User not found.")
        else:
            print(f"❌ Error: {response.status_code} - {response.reason}")
    except requests.RequestException as e:
        print(f"❌ Network error: {e}")
    return None

def display_profile(data):
    print("\n👤 GitHub Profile Info:")
    print(f"Username     : {data.get('login')}")
    print(f"Name         : {data.get('name') or 'N/A'}")
    print(f"Bio          : {data.get('bio') or 'N/A'}")
    print(f"Location     : {data.get('location') or 'N/A'}")
    print(f"Public Repos : {data.get('public_repos')}")
    print(f"Followers    : {data.get('followers')}")
    print(f"Following    : {data.get('following')}")
    print(f"Profile Link : {data.get('html_url')}")
    print(f"Created At   : {data.get('created_at')}")
    print(f"Avatar URL   : {data.get('avatar_url')}")

def main():
    print("🐙 GitHub Profile Fetcher")
    username = input("Enter GitHub username: ").strip()
    if not username:
        print("❌ Username cannot be empty.")
        return
    
    data = fetch_profile(username)
    if data:
        display_profile(data)

if __name__ == "__main__":
    main()
