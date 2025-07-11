import requests
import random
import time

def generate_fake_email():
    user = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890', k=10))
    return f"bot-{user}@example.com"

def ping():
    url = "https://landingpagebackend-df79.onrender.com/api/subscribe"
    email = generate_fake_email()
    payload = { "email": email }
    headers = { "Content-Type": "application/json" }

    try:
        response = requests.post(url, json=payload, headers=headers)
        print(f"[{time.ctime()}] Sent: {email} - Status: {response.status_code} - Message: {response.json().get('message')}")
    except Exception as e:
        print(f"[{time.ctime()}] Error: {e}")

while True:
    ping()
    delay = random.randint(300, 840)  # 5–14 minutes
    print(f"Next ping in {delay // 60}m {delay % 60}s\n")
    time.sleep(delay)
