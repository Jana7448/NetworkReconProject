import os
import nmap

import sys

if len(sys.argv) > 1:
    target = sys.argv[1]
else:
    target = input("Enter Target (IP or Domain): ")


scanner = nmap.PortScanner()

print("\nScanning, please wait...\n")

try:
    scanner.scan(target, '1-1000')

    base_dir = os.path.dirname(os.path.abspath(__file__))
    report_dir = os.path.join(base_dir, "..", "reports")
    os.makedirs(report_dir, exist_ok=True)

    report_path = os.path.join(report_dir, "nmap_report.txt")

    with open(report_path, "w") as file:

        file.write("Nmap Scan Report\n")
        file.write("========================\n")
        file.write(f"Target: {target}\n\n")

        for host in scanner.all_hosts():

            file.write(f"Host: {host}\n")
            print(f"Host: {host}")

            for protocol in scanner[host].all_protocols():

                file.write(f"\nProtocol: {protocol}\n")

                ports = sorted(scanner[host][protocol].keys())

                for port in ports:

                    state = scanner[host][protocol][port]["state"]

                    if state == "open":
                        print(f"Port {port}: OPEN")
                        file.write(f"Port {port}: OPEN\n")

    print("\nScan completed successfully.")
    print(f"Report saved to: {report_path}")

except Exception as e:
    print("Error:", e)
