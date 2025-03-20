import os
import re
import csv
from datetime import datetime  # Verify and/or create a nifty timestamp

def list_logs():
    log_dir = "/var/log"
    findings = []
    try:
        for log_file in os.listdir(log_dir):
            if log_file.endswith(".log"):
                file_path = os.path.join(log_dir, log_file)
                try:
                    with open(file_path, "r") as f:
                        for line in f:
                            if re.search(r'fail|error|timeout', line, re.IGNORECASE):
                                # Extract timestamp if present, else use current time
                                timestamp_match = re.search(r'^\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}', line)
                                timestamp = timestamp_match.group(0) if timestamp_match else datetime.now().strftime("%b %d %H:%M:%S")
                                message = line.strip()
                                findings.append((timestamp, file_path, message))
                except PermissionError:
                    findings.append((datetime.now().strftime("%b %d %H:%M:%S"), file_path, "Permission denied"))
                except FileNotFoundError:
                    findings.append((datetime.now().strftime("%b %d %H:%M:%S"), file_path, "File not found"))
                except Exception as e:
                    findings.append((datetime.now().strftime("%b %d %H:%M:%S"), file_path, f"Error reading: {e}"))
    except PermissionError:
        findings.append((datetime.now().strftime("%b %d %H:%M:%S"), log_dir, "Permission denied accessing directory"))
    except Exception as e:
        findings.append((datetime.now().strftime("%b %d %H:%M:%S"), log_dir, f"Directory error: {e}"))
    
    # Write to CSV
    csv_path = os.path.expanduser("Desktop/class/errors.csv")
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)  # Create dir if needed
    print(f"Writing to: {csv_path}")
    with open(csv_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Timestamp", "File", "Message"])  # Header
        writer.writerows(findings)
        print(f"Wrote {len(findings)} rows to {csv_path}")
    
    return findings

# Test it
if __name__ == "__main__":
    results = list_logs()
    for timestamp, file_path, message in results:
        print(f"I found THIS: {timestamp} | {file_path} | {message}")
