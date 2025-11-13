from flask import Flask, render_template, request
import requests, re
from bs4 import BeautifulSoup

app = Flask(__name__)

def check_vulns(url):
    results = []
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        if re.search(r"sql|mysql|database", response.text, re.IGNORECASE):
            results.append(f"{url} may be vulnerable to SQL Injection")

        if re.search(r"<script>", response.text, re.IGNORECASE):
            results.append(f"{url} may be vulnerable to XSS")

        if re.search(r"wordpress|joomla|drupal", response.text, re.IGNORECASE):
            results.append(f"{url} may be running outdated software")

        if not results:
            results.append("No obvious vulnerabilities detected.")
    except Exception as e:
        return [], f"Error: {e}"

    return results, None


@app.route("/", methods=["GET", "POST"])
def vuln_checker():
    results = []
    error = None
    if request.method == "POST":
        url = request.form.get("url")
        results, error = check_vulns(url)
    return render_template("vuln_checker.html", results=results, error=error)


if __name__ == "__main__":
    app.run(debug=True)
