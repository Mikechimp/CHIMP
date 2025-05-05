import sys
from scanner import passive_recon  # Make sure scanner.py has passive_recon()
from openai_support import summarize_scan
from utils import is_valid_ip

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <IP>")
        return

    ip = sys.argv[1]

    if not is_valid_ip(ip):
        print("❌ Invalid IP address format.")
        return

    print(f"\n🧠 Performing passive recon on {ip}...")
    recon_data = passive_recon(ip)

    print("\n📄 Raw Recon Results:")
    for section, data in recon_data.items():
        print(f"\n🔹 {section}")
        for k, v in data.items():
            print(f"  {k}: {v}")

    print("\n🤖 AI Summary:")
    # Flatten the recon data into a string for AI input
    formatted = "\n".join(
        f"{section}:\n" + "\n".join(f"  {k}: {v}" for k, v in details.items())
        for section, details in recon_data.items()
    )
    summary = summarize_scan(formatted)
    print(summary)

if __name__ == "__main__":
    main()

