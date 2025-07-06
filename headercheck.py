import requests
import argparse

# Headers to check
required_headers = {
    "Content-Security-Policy": "Prevents XSS by defining content rules",
    "Strict-Transport-Security": "Forces HTTPS connections",
    "X-Content-Type-Options": "Prevents MIME sniffing",
    "X-Frame-Options": "Blocks clickjacking via iframes",
    "Referrer-Policy": "Controls referrer info sent",
    "Permissions-Policy": "Limits use of browser features (e.g., camera, mic)"
}

def analyze_headers(url):
    print(f"\n🔍 Analyzing headers for: {url}\n")
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        found = []
        missing = []

        for header, reason in required_headers.items():
            if header in headers:
                found.append((header, headers[header]))
            else:
                missing.append((header, reason))

        print("✅ Found Headers:")
        for h, v in found:
            print(f"  - {h}: {v[:100]}")

        print("\n❌ Missing Headers:")
        for h, why in missing:
            print(f"  - {h}: {why}")

        return found, missing

    except Exception as e:
        print("❌ Error fetching URL:", str(e))
        return [], []

def main():
    parser = argparse.ArgumentParser(description="🔐 HeaderCheck - HTTP Security Header Analyzer")
    parser.add_argument("-u", "--url", required=True, help="Target URL to check")
    parser.add_argument("-o", "--output", help="Save results to this file")
    args = parser.parse_args()

    found, missing = analyze_headers(args.url)

    if args.output:
        with open(args.output, "w") as f:
            f.write(f"Header Analysis for {args.url}\n\n")
            f.write("✅ Found Headers:\n")
            for h, v in found:
                f.write(f"{h}: {v}\n")
            f.write("\n❌ Missing Headers:\n")
            for h, reason in missing:
                f.write(f"{h}: {reason}\n")
        print(f"\n📁 Results saved to: {args.output}")

if __name__ == "__main__":
    main()
