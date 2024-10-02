import requests
from bs4 import BeautifulSoup
import os
import sys
import argparse
from urllib.parse import urljoin

# Argument Parsing for Dynamic Input
parser = argparse.ArgumentParser(description="Advanced Web Crawler")
parser.add_argument("-d", "--domain", required=True, help="Target domain to crawl")
parser.add_argument("-o", "--output", help="File to save crawled links")
args = parser.parse_args()

domain = args.domain
output_file = args.output if args.output else f'recon/{domain}/crawler_output'

# Ensure Recon Directory Exists
os.makedirs(f'recon/{domain}', exist_ok=True)

content_list = []
session = requests.Session()

def request(url):
    try:
        response = session.get(url, allow_redirects=False, timeout=5)
        return response.content
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ''

def crawl(url):
    html = request(url)
    if not html:
        return
    soup = BeautifulSoup(html, 'html.parser')
    for a in soup.find_all('a', href=True):
        link = urljoin(url, a['href'])
        if '#' in link:
            link = link.split('#')[0]  # Remove URL fragment
        if link not in content_list and domain in link:
            content_list.append(link)
            print(f"[+] Found URL: {link}")
            with open(output_file, 'a') as file:
                file.write(link + '\n')
            crawl(link)

def load_subdomains():
    subdomains_file = f'recon/{domain}/subdomains'
    if os.path.exists(subdomains_file):
        with open(subdomains_file, 'r') as file:
            return file.read().splitlines()
    return [domain]

if __name__ == "__main__":
    subdomains = load_subdomains()
    for subdomain in subdomains:
        url = f"http://{subdomain}"
        crawl(url)
