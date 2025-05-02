def format_ports(port_list):
    """Returns a clean string of open ports."""
    if not port_list:
        return "No open ports found (excluding 80 and 443)."
    return "Open Ports: " + ", ".join(str(p) for p in port_list)


def is_valid_ip(ip):
    """Basic validation to check if IP format is correct."""
    import re
    pattern = r"^\d{1,3}(\.\d{1,3}){3}$"
    return re.match(pattern, ip) is not None

