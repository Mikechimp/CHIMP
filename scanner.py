import subprocess

def scan_ports(ip):
    try:
        # Run AutoRecon against the target IP
        result = subprocess.run(
            ["autorecon", ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        return result.stdout  # This is the full AutoRecon output

    except subprocess.CalledProcessError as e:
        return f"AutoRecon failed: {e.output}"

