import sys
from scanner import scan_ports
from openai_support import summarize_scan

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <IP>")
        return

    ip = sys.argv[1]
    print(f"Scanning IP: {ip}...")
    result = scan_ports(ip)
    print("\n--- RAW SCAN OUTPUT ---\n")
    print(result)

    print("\n--- AI SUMMARY ---\n")
    summary = summarize_scan(result)
    print(summary)

if __name__ == "__main__":
    main()

