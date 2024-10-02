import requests
import threading
import queue
import sys
import os
import argparse

# Argument Parsing
parser = argparse.ArgumentParser(description="Advanced Directory Buster")
parser.add_argument("-u", "--url", required=True, help="Target URL")
parser.add_argument("-t", "--threads", type=int, default=10, help="Number of threads")
parser.add_argument("-e", "--ext", help="Optional file extension to append")
args = parser.parse_args()

host = args.url
threads = args.threads
ext = args.ext
directory_list = 'wordlists/common.txt'
recon_dir = f"recon/{host.split('/')[2]}"

# Ensure Recon Directory Exists
os.makedirs(recon_dir, exist_ok=True)

q = queue.Queue()

print("[+] Starting directory brute-forcing...")

def dirbuster(thread_no, q):
    while not q.empty():
        url = q.get()
        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                print(f"[+] Directory found: {url}")
                with open(f'{recon_dir}/directory_buster_output', 'a') as file:
                    file.write(f"{url}\n")
        except Exception:
            pass
        q.task_done()

# Load Directories from Wordlist
with open(directory_list, 'r') as file:
    for directory in file.read().splitlines():
        if ext:
            q.put(f"{host}/{directory}.{ext}")
        else:
            q.put(f"{host}/{directory}")

# Run Threads
for _ in range(threads):
    t = threading.Thread(target=dirbuster, args=(0, q), daemon=True)
    t.start()

q.join()
