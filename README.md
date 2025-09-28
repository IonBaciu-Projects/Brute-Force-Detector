# Brute-Force-Detector

A lightweight Python log analysis tool that detects brute-force login attempts and suspicious requests (SQLi/XSS) from server logs.

---

## Features
- Detects repeated failed `POST /login` attempts (default threshold = 3)
- Detects simple SQL injection and XSS patterns in request lines
- Prints flagged IPs and suspicious request lines
- Single-file script: `Log-Analyzer.py`

---

## Installation

1. Clone the repo:
```bash
git clone https://github.com/YOUR_USERNAME/Brute-Force-Detector.git
cd Brute-Force-Detector
