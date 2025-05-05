import socket

def scan_ports(ip, ports_to_check):
    open_ports = []
    print(f"\n🔍 Scanning {ip}...\n")
    
    for port in ports_to_check:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((ip, port))
                if result == 0:
                    open_ports.append(port)
                    print(f"✅ Port {port} is open")
                else:
                    print(f"❌ Port {port} is closed")
        except Exception as e:
            print(f"⚠️ Error scanning port {port}: {e}")
    
    print("\n🎯 Scan Complete")
    return open_ports

# Define IP and custom port list (excluding 80 and 443)
target_ip = "198.248.86.124"
custom_ports = [21, 22, 23, 25, 53, 110, 135, 139, 143, 445, 3306, 3389]  # Add/remove as needed

results = scan_ports(target_ip, custom_ports)
print(f"\n📄 Open Ports: {results}")

