# Web-Security-Tools

This repository contains a collection of advanced Python-based tools for web security testing. These tools cover tasks such as web crawling, subdomain discovery, directory busting, HTTP password guessing, web vulnerability scanning (e.g., SQLi and XSS), and Slack integration for notifications.

## Tools Included

1. **Web Crawler**  
   A tool that crawls a target website, finding all internal links.

2. **Subdomain Discovery**  
   Bruteforce subdomains of a target domain to identify new hosts.

3. **Directory Buster**  
   Bruteforce directories on the target website to identify hidden paths.

4. **HTTP Password Guesser**  
   A tool for brute-forcing passwords for HTML forms on web applications.

5. **Web Vulnerability Scanner**  
   Scan a website for SQL Injection (SQLi) and Cross-Site Scripting (XSS) vulnerabilities.

6. **Slack Notifications**  
   Automatically post scan results to a Slack channel via a webhook.

---

## Installation

You will need **Python 3** to run these tools. Install the necessary dependencies by running:

```bash
pip install -r requirements.txt
```

### Dependencies:
- `requests`: For making HTTP requests and interacting with web pages.
- `beautifulsoup4`: For parsing HTML to extract forms and links.
- `colorama`: For colorized terminal output.
- `urllib3`: For handling HTTP connections.
- `argparse`: For command-line argument handling.
  
## Usage

Each tool is a standalone Python script that can be executed from the command line. Below are detailed usage examples for each tool.

### 1. Web Crawler

This tool crawls a website and extracts all internal links.

#### Usage:
```bash
python3 web_crawler.py -d <domain> [-o <output_file>]
```

- `-d`: The target domain to crawl (e.g., `example.com`).
- `-o`: (Optional) File to save the crawled links.

#### Example:
```bash
python3 web_crawler.py -d example.com -o output.txt
```

---

### 2. Subdomain Discovery

This tool brute-forces subdomains for a given domain and checks their availability using HTTP requests.

#### Usage:
```bash
python3 subdomain_discovery.py -d <domain> [-t <threads>]
```

- `-d`: The target domain to discover subdomains for.
- `-t`: (Optional) Number of threads to use (default: 10).

#### Example:
```bash
python3 subdomain_discovery.py -d example.com -t 20
```

---

### 3. Directory Buster

This tool brute-forces directories on the target website.

#### Usage:
```bash
python3 directory_buster.py -u <url> [-t <threads>] [-e <ext>]
```

- `-u`: The target URL.
- `-t`: (Optional) Number of threads (default: 10).
- `-e`: (Optional) File extension to append (e.g., `.php`, `.html`).

#### Example:
```bash
python3 directory_buster.py -u http://example.com -t 20 -e php
```

---

### 4. HTTP Password Guesser

This tool brute-forces passwords for an HTML form using the HTTP GET or POST method.

#### Usage:
```bash
python3 http_password_guesser.py -u <url> -d <data> -m <method> -f <field> -s <success_message> -t <threads>
```

- `-u`: The target URL of the form action.
- `-d`: Query string or POST body data.
- `-m`: HTTP method (GET or POST).
- `-f`: The field name to brute force (e.g., password).
- `-s`: Success message upon a correct password (unique string).
- `-t`: (Optional) Number of threads to use.

#### Example:
```bash
python3 http_password_guesser.py -u http://example.com/login -d "username=admin&password=" -m POST -f password -s "Welcome" -t 5
```

---

### 5. Web Vulnerability Scanner

This tool scans a target website for SQL Injection (SQLi) and Cross-Site Scripting (XSS) vulnerabilities.

#### Usage:
```bash
python3 vuln_scanner.py -d <domain>
```

- `-d`: The target domain to scan for vulnerabilities.

#### Example:
```bash
python3 vuln_scanner.py -d example.com
```

---

### 6. Slack Notifications

This tool posts scan results to a Slack channel via a webhook.

#### Usage:
```bash
python3 slack_notifier.py -d <domain>
```

- `-d`: The target domain whose results are being posted to Slack.

#### Example:
```bash
python3 slack_notifier.py -d example.com
```

---

## Requirements

Install the necessary Python libraries by running:

```bash
pip install -r requirements.txt
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Disclaimer

These tools are intended for educational and research purposes only. Use them only on systems and networks where you have explicit permission to perform security testing. The author is not responsible for any misuse or damages caused by using these tools.

---

## Contact

If you have any questions, feel free to reach out via GitHub issues or email.

---

## Acknowledgments

Thanks to the developers of the libraries used in this project, such as **requests**, **beautifulsoup4**, and **colorama**.

---

## Future Improvements

Here are some potential future improvements for these tools:

1. **Integration with a GUI Interface**  
   Adding a web-based dashboard or a graphical interface to make the tools more user-friendly and allow real-time interaction.

2. **Support for More Vulnerabilities**  
   Expand the Web Vulnerability Scanner to cover additional types of vulnerabilities, such as:
   - **CSRF (Cross-Site Request Forgery)**
   - **Open Redirects**
   - **Command Injection**
   - **File Inclusion Vulnerabilities**

3. **Automated Reporting**  
   Add features to generate comprehensive reports after a scan in formats like PDF or CSV, which can be useful for documentation and sharing results.

4. **Better Slack Integration**  
   Enable more detailed and formatted Slack notifications, such as attaching files, formatting results in a table, and including screenshots of the results.

5. **More Wordlists for Subdomain and Directory Brute-forcing**  
   Include or integrate with larger and more specialized wordlists for better coverage in subdomain and directory brute-forcing.

6. **Multi-Platform Support**  
   Ensure seamless compatibility across different platforms (Linux, Windows, macOS) by resolving any OS-specific issues.

7. **Plugin System**  
   Allow users to write their own plugins for extending the tools, adding more functionality without modifying the core codebase.

8. **Optimized Threading for Large Scale Testing**  
   Implement optimized threading and possibly asynchronous programming to handle very large-scale testing across multiple domains or services in parallel.

9. **Rate Limiting Handling**  
   Add mechanisms to detect and bypass rate-limiting and captchas during scanning, particularly for high-security or high-traffic websites.

10. **Integration with Other Services**  
    - **Shodan API** for gathering information about exposed services.
    - **Have I Been Pwned API** to detect if credentials found during brute-forcing are already compromised.

---
