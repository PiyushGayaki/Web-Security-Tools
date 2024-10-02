# Web Security Tools

This repository contains tools for web security assessments, including web crawling, subdomain discovery, directory busting, and vulnerability scanning.

## Tools Overview

### 1. Web Crawler (`web_crawler.py`)
- Crawls a website and gathers all internal and external URLs.
- **Usage**: `python3 web_crawler.py <domain>`

### 2. Subdomain Discovery (`fast_subdomain_finder.py`)
- Brute-forces subdomains using a wordlist and checks for valid subdomains.
- **Usage**: `python3 fast_subdomain_finder.py <domain> <threads>`

### 3. Directory Busting (`fast_directory_buster.py`)
- Scans a website for hidden directories using a wordlist.
- **Usage**: `python3 fast_directory_buster.py http://<target> <threads>`

### 4. Web Vulnerability Scanner (`web_vulnerability_scanner.py`)
- Scans a website for SQL Injection and XSS vulnerabilities.
- **Usage**: `python3 web_vulnerability_scanner.py <domain>`
