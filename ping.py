import time
import random
import requests
from datetime import datetime
import os

# File to store logs
LOG_FILE = "ping_log.txt"

# List of URLs to ping (only use sites you own or have permission for)
URLS = [
    "https://catterpiweb-learn.onrender.com",
    "https://catterpiweb-learn.onrender.com",
    # add more here
]

def log(message):
    """Write a message to both console and log file."""
    print(message)
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")

# Chance to skip this entire run (e.g., 30%)
if random.random() < 0.3:
    log(f"{datetime.now()} | Skipping this run for more natural pattern.")
    exit()

def send_request(url):
    try:
        r = requests.get(url)
        log(f"{datetime.now()} | {url} | Status: {r.status_code}")
    except Exception as e:
        log(f"{datetime.now()} | {url} | Error: {e}")

# First request: random delay 0–7 min
delay_1 = random.randint(0, 7 * 60)
time.sleep(delay_1)
send_request(random.choice(URLS))

# Second request: random delay 0–7 min
delay_2 = random.randint(0, 7 * 60)
time.sleep(delay_2)
send_request(random.choice(URLS))
