import re
import os

# IPv4 pattern: matches xxx.xxx.xxx.xxx
IP_REGEX = r"\b\d{1,3}(?:\.\d{1,3}){3}\b"

def extract_ips(file_path):
    if not os.path.exists(file_path):
        print("❌ Error: File does not exist.")
        return []

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    ips = re.findall(IP_REGEX, content)
    
    # Optional: filter only valid IPv4 addresses
    valid_ips = [ip for ip in ips if all(0 <= int(part) <= 255 for part in ip.split('.'))]
    
    return sorted(set(valid_ips))  # Remove duplicates and sort

def main():
    print("📄 Log File IP Extractor")
    file_path = input("Enter path to log file: ").strip()

    ip_list = extract_ips(file_path)
    if ip_list:
        print(f"\n✅ Found {len(ip_list)} unique IP address(es):")
        for ip in ip_list:
            print(" -", ip)

        save = input("\n💾 Save results to 'ips.txt'? (y/n): ").lower()
        if save == 'y':
            with open("ips.txt", "w") as f:
                for ip in ip_list:
                    f.write(ip + "\n")
            print("📁 Saved to ips.txt")
    else:
        print("⚠️ No IP addresses found.")

if __name__ == "__main__":
    main()
