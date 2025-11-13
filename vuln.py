import requests
from bs4 import BeautifulSoup
import re

def check_vulns(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Check for SQL Injection vulnerabilities
        if re.search(r"sql|mysql|database", response.text, re.IGNORECASE):
            print(f"{url} may be vulnerable to SQL Injection")
        
        # Check for Cross-Site Scripting (XSS) vulnerabilities
        if re.search(r"<script>", response.text, re.IGNORECASE):
            print(f"{url} may be vulnerable to XSS")
        
        # Check for outdated software
        if re.search(r"wordpress|joomla|drupal", response.text, re.IGNORECASE):
            print(f"{url} may be running outdated software")
        
    except Exception as e:
        print(f"Error: {e}")

url = input("Enter a URL: ")
check_vulns(url)
