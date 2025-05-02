import subprocess

def scan_ports(ip):
    print(f"\n🚀 Starting AutoRecon on {ip}...\n")
    try:
        # Run AutoRecon against the target IP
        process = subprocess.Popen(
            ["autorecon", ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True        
        )
 # Live output loop
        output_lines = []
        for line in process.stdout:
            print(line.strip())  # Real-time output to terminal
            output_lines.append(line)

        process.wait()

        print(f\n Auto recon complete for [ip]\n")
        return "".join(output_lines)

    
    except Exception as e:
        return f"❌ AutoRecon failed: {str(e)}"
