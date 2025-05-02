import sys
from scanner import scan_ports
from openai_support import summarize_scan
from utils import format_ports, is_valid_ip

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <IP>")
        return

    ip = sys.argv[1]

    if not is_valid_ip(ip):
        print("Invalid IP address format.")
        return

    print(f"\n🔍 Scanning {ip} for open ports (excluding 80 and 443)...")
    open_ports = scan_ports(ip)

    formatted = format_ports(open_ports)
    print("\n📄 Scan Results:")
    print(formatted)

    print("\n🤖 AI Summary:")
    summary = summarize_scan(formatted)
    print(summary)

if __name__ == "__main__":
    main()

