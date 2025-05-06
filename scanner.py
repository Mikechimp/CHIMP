import os
import requests
from dotenv import load_dotenv

load_dotenv()

ABUSE_KEY = os.getenv("ABUSEIPDB_API_KEY")
SHODAN_KEY = os.getenv("SHODAN_API_KEY")

def get_abuseipdb_report(ip):
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        "Key": ABUSE_KEY,
        "Accept": "application/json"
    }
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()["data"]
        return {
            "Abuse Score": data.get("abuseConfidenceScore"),
            "Country": data.get("countryCode"),
            "Usage Type": data.get("usageType"),
            "ISP": data.get("isp"),
            "Domain": data.get("domain"),
            "Total Reports": data.get("totalReports"),
            "Last Reported": data.get("lastReportedAt"),
        }
    else:
        return {"Error": f"AbuseIPDB Error: {response.text}"}


def get_shodan_data(ip):
    url = f"https://api.shodan.io/shodan/host/{ip}?key={SHODAN_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "Organization": data.get("org"),
            "ISP": data.get("isp"),
            "Operating System": data.get("os"),
            "Open Ports": data.get("ports"),
            "Vulnerabilities": data.get("vulns", "None listed"),
        }
    else:
        return {"Error": f"Shodan Error: {response.text}"}


def passive_recon(ip):
    try:
        abuse_data = get_abuseipdb_report(ip)
        shodan_data = get_shodan_data(ip)

        return {
            "AbuseIPDB": abuse_data,
            "Shodan": shodan_data
        }

    except Exception as e:
        print(f"❌ Passive recon error: {e}")
        return None



