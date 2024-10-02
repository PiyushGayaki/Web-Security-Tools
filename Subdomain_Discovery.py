import requests
import threading
import queue
import os
import argparse

# Argument Parsing
parser = argparse.ArgumentParser(description="Advanced Subdomain Brute Forcer")
parser.add_argument("-d", "--domain", required=True, help="Target domain")
parser.add_argument("-t", "--threads", type=int, default=10, help="Number of threads")
args = parser.parse_args()

host = args.domain
threads = args.threads
recon_dir = f'recon/{host}'

# Ensure Recon Directory Exists
os.makedirs(recon_dir, exist_ok=True)

q = queue.Queue()

print("[+] Starting subdomain brute-forcing...")

def subbruteforcer():
    while not q.empty():
        subdomain = q.get()
        url = f"https://{subdomain}.{host}"
        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                subd = response.url.split('/')[2]
                print(f"[+] Subdomain found: {subd}")
                with open(f'{recon_dir}/subdomains', 'a') as file:
                    file.write(subd + '\n')
        except Exception:
            pass
        q.task_done()

# Load Subdomains from Wordlist
with open('wordlists/subdomain_list_large', 'r') as file:
    for subdomain in file.read().splitlines():
        q.put(subdomain)

# Run Threads
for _ in range(threads):
    t = threading.Thread(target=subbruteforcer, daemon=True)
    t.start()

q.join()
