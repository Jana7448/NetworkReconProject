import subprocess

def banner():
    print("=" * 60)
    print("   NETWORK RECONNAISSANCE AND SECURITY ASSESSMENT TOOL")
    print("=" * 60)

def menu():
    print("\nChoose an Option")
    print("1. Host Discovery")
    print("2. Port Scanner")
    print("3. DNS Lookup")
    print("4. WHOIS Lookup")
    print("5. Nmap Scan")
    print("6. Run All")
    print("0. Exit")

banner()

while True:
    menu()

    choice = input("\nEnter your choice: ")

    if choice == "1":
        subprocess.run(["python3", "scripts/host_discovery.py"])

    elif choice == "2":
        subprocess.run(["python3", "scripts/port_scanner.py"])

    elif choice == "3":
        subprocess.run(["python3", "scripts/dns_lookup.py"])

    elif choice == "4":
        subprocess.run(["python3", "scripts/whois_lookup.py"])

    elif choice == "5":
        subprocess.run(["python3", "scripts/nmap_scan.py"])

    elif choice == "6":
        target = input("\nEnter Target (Domain/IP): ")

        print("\nRunning Host Discovery...")
        subprocess.run(["python3", "scripts/host_discovery.py", target])

        print("\nRunning Port Scanner...")
        subprocess.run(["python3", "scripts/port_scanner.py", target])

        print("\nRunning DNS Lookup...")
        subprocess.run(["python3", "scripts/dns_lookup.py", target])

        print("\nRunning WHOIS Lookup...")
        subprocess.run(["python3", "scripts/whois_lookup.py", target])

        print("\nRunning Nmap Scan...")
        subprocess.run(["python3", "scripts/nmap_scan.py", target])

        print("\nAll operations completed successfully.")

    elif choice == "0":
        print("\nThank you for using the tool.")
        break

    else:
        print("\nInvalid Choice! Please try again.")
