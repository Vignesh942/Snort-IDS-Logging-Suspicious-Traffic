import time
import re

# Path to Snort configuration file
SNORT_CONF = "/etc/snort/snort.conf"

# Path to Snort alert log file (Update this if different)
LOG_FILE = "/var/log/snort/snort.alert.fast"

# Define patterns to detect specific Nmap scans
SCAN_PATTERNS = {
    "SYN Scan": r"Nmap SYN Scan detected",
    "FIN Scan": r"Nmap FIN Scan detected",
    "XMAS Scan": r"Nmap XMAS Scan detected",
    "NULL Scan": r"Nmap NULL Scan detected",
    "UDP Scan": r"Nmap UDP Scan detected",
    "Version Detection": r"Nmap Version Detection Scan detected",
    "OS Detection": r"Nmap OS Detection Scan detected",
    "Ping Scan": r"Nmap Ping Scan detected",
}

def monitor_snort_logs():
    """Continuously monitor Snort logs for Nmap scan detection."""
    print(f"[*] Using Snort configuration from: {SNORT_CONF}")
    print("[*] Monitoring Snort logs for Nmap scans...")

    with open(LOG_FILE, "r") as log_file:
        log_file.seek(0, 2)  # Move to end of file

        while True:
            line = log_file.readline()
            if not line:
                time.sleep(1)  # Wait for new log entries
                continue

            # Check if the log matches any known Nmap scan pattern
            for scan_type, pattern in SCAN_PATTERNS.items():
                if re.search(pattern, line):
                    print(f"[ALERT] {scan_type} detected: {line.strip()}")

if __name__ == "__main__":
    monitor_snort_logs()
