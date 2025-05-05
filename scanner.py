import subprocess

def scan_ports(ip):
    print(f"\n🔍 Starting Netcat scan on {ip}...\n")
    ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080]
    output_lines = []

    try:
        for port in ports_to_scan:
            print(f"Scanning port {port}...")
            result = subprocess.run(
                ["ncat", "-zv", ip, str(port)],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )
            print(result.stdout.strip())
            output_lines.append(result.stdout)

        print(f"\n✅ Netcat scan complete for {ip}\n")
        return "".join(output_lines)

    except Exception as e:
        return f"❌ Netcat scan failed: {str(e)}"

