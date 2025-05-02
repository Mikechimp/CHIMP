import subprocess

def scan_ports(ip, start_port=1, end_port=1024):
    open_ports = []

    for port in range(start_port, end_port + 1):
        if port in (80, 443):  # Skip 80 and 443
            continue

        result = subprocess.run(
            ["nc", "-zv", "-w", "1", ip, str(port)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True
        )

        if "succeeded" in result.stderr:
            open_ports.append(port)

    return open_ports

