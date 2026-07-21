import whois

import sys

if len(sys.argv) > 1:
    target = sys.argv[1]
else:
    target = input("Enter Target: ")

domain = target


try:

    info = whois.whois(domain)

    print(info)

    report_path = "reports/whois_report.txt"

    with open(report_path, "w") as file:
        file.write(str(info))

    print("\nReport saved successfully.")

except Exception as e:

    print("Error:", e)
