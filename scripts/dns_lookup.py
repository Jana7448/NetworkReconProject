import socket

import sys

if len(sys.argv) > 1:
    target = sys.argv[1]
else:
    target = input("Enter Target: ")

domain = target


try:
    ip = socket.gethostbyname(domain)

    print(f"\nIP Address: {ip}")

    report_path = "reports/dns_report.txt"

    with open(report_path, "w") as file:
        file.write("DNS Lookup Report\n")
        file.write("========================\n")
        file.write(f"Domain : {domain}\n")
        file.write(f"IP Address : {ip}\n")

    print("Report saved successfully.")

except socket.gaierror:
    print("Invalid domain.")
