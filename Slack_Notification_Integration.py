import json
import requests
import argparse

# Argument Parsing
parser = argparse.ArgumentParser(description="Slack Notification Tool")
parser.add_argument("-d", "--domain", required=True, help="Target domain")
args = parser.parse_args()

domain = args.domain
slack_webhook_url = "your-slack-webhook-url"

def send_to_slack(message):
    data = {'text': message}
    response = requests.post(slack_webhook_url, json=data)
    if response.status_code == 200:
        print("[+] Message posted to Slack")
    else:
        print(f"[-] Failed to post message: {response.status_code}")

if __name__ == "__main__":
    with open(f"recon/{domain}/vuln_scanner_results", 'r') as file:
        result = file.read()
    send_to_slack(result)
