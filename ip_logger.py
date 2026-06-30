import requests
import datetime

def get_public_ip():
    try:
        # Use ipify service to get the public IP
        response = requests.get('https://api.ipify.org?format=json', timeout=5)
        response.raise_for_status()
        ip_data = response.json()
        return ip_data['ip']
    except requests.exceptions.RequestException as e:
        return f"Error fetching IP: {e}"

def save_ip_to_file(ip_address, filename="my_ips.txt"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"Date: {timestamp} | IP Address: {ip_address}\n"

    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(log_entry)
        print(f"IP address successfully saved to {filename}.")
    except IOError as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    current_ip = get_public_ip()
    print(f"Your IP address: {current_ip}")

    if not current_ip.startswith("Error"):
        save_ip_to_file(current_ip)
    else:
        print("Skipping save, since fetching IP failed.")