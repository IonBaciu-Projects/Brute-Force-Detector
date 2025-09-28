import re
import sys
from collections import defaultdict

def analyze_log(filename, threshold=3):
    failed_logins = defaultdict(int)
    suspicious_requests = []

    failed_login_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+).+"POST /login.*" 401')
    sql_injection_pattern = re.compile(r"(?:' OR '1'='1|<script>|UNION SELECT)", re.IGNORECASE)

    try:
        with open(filename, "r") as f:
            for line in f:
                match = failed_login_pattern.search(line)
                if match:
                    ip = match.group(1)
                    failed_logins[ip] += 1

                if sql_injection_pattern.search(line):
                    suspicious_requests.append(line.strip())

    except FileNotFoundError:
        print(f"File not found: {filename}")
        return

    print("\n=== Brute Force Attempts ===")
    for ip, count in failed_logins.items():
        if count >= threshold:
            print(f"[!] {ip} had {count} failed login attempts")

    print("\n=== Suspicious Requests (SQLi/XSS) ===")
    if suspicious_requests:
        for req in suspicious_requests:
            print(f"[!] {req}")
    else:
        print("No suspicious requests detected.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python log_analyzer.py <logfile>")
    else:
        analyze_log(sys.argv[1])