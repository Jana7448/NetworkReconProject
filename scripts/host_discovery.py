import subprocess
import platform

import sys

if len(sys.argv) > 1:
    target = sys.argv[1]
else:
    target = input("Enter Target: ")

if platform.system().lower() == "windows":
    command = ["ping", "-n", "4", target]
else:
    command = ["ping", "-c", "4", target]

print("\nScanning...\n")

result = subprocess.run(command, capture_output=True, text=True)

print(result.stdout)

if result.returncode == 0:
    status = "Host is UP"
else:
    status = "Host is DOWN"

print(status)

report_path = "reports/host_report.txt"


with open(report_path, "w") as file:
    file.write("Host Discovery Report\n")
    file.write("=========================\n")
    file.write(f"Target : {target}\n\n")
    file.write(result.stdout)
    file.write("\n")
    file.write(status)

print("\nReport saved successfully.")
