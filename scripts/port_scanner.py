import socket

import sys

if len(sys.argv) > 1:
    target = sys.argv[1]
else:
    target = input("Enter Target: ")

ports = [21, 22, 23, 25, 53, 80, 110, 143, 443]

print(f"\nScanning {target}...\n")

open_ports = []

for port in ports:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")
        open_ports.append(port)

    s.close()

report_path = "reports/port_report.txt"

with open(report_path, "w") as file:

    file.write("Port Scanner Report\n")
    file.write("========================\n")
    file.write(f"Target : {target}\n\n")

    if open_ports:
        file.write("Open Ports\n")

        for port in open_ports:
            file.write(f"{port}\n")
    else:
        file.write("No open ports found.\n")

print("\nReport saved successfully.")
