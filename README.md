# 🔐 HeaderCheck – HTTP Security Header Analyzer

**HeaderCheck** is a Python tool to analyze web responses for the presence of critical security headers.

## 🚀 Checks for:

- Content-Security-Policy
- Strict-Transport-Security
- X-Content-Type-Options
- X-Frame-Options
- Referrer-Policy
- Permissions-Policy

## 📦 Features

- Detects missing security headers
- Explains why each header is important
- Saves output to file
- No external libraries required (uses `requests`)

## 🛠️ Usage

```bash
python headercheck.py -u https://example.com -o report.txt
