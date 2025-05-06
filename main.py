import sys
import argparse
from scanner import passive_recon
from openai_support import summarize_scan
from utils import is_valid_ip
from spiderfoot_parser import parse_spiderfoot_csv

def main():
    parser = argparse.ArgumentParser(description="Recon Reporter")
    parser.add_argument("target", help="Target IP address or file path")
    parser.add_argument("--spidermap", help="Optional SpiderFoot output file (CSV)")

    args = parser.parse_args()

    if not is_valid_ip(args.target):
        print("❌ Invalid IP format.")
        return

    print(f"\n🧠 Performing passive recon on {args.target}...")
    recon_data = passive_recon(args.target)

    if not recon_data:
        print("❌ Recon failed.")
        return

    # OPTIONAL: parse and append SpiderFoot CSV data
    if args.spidermap:
        spider_results = parse_spiderfoot_csv(args.spidermap)
        recon_data["SpiderFoot"] = spider_results

    print("\n🤖 AI-Powered Recon Summary (Chunked):\n")
    summary = summarize_scan(recon_data)
    print(summary)

if __name__ == "__main__":
    main()
