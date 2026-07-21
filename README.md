# Network Reconnaissance and Security Assessment Tool

## Project Overview

The Network Reconnaissance and Security Assessment Tool is a Python-based cybersecurity project developed to perform basic network reconnaissance tasks. It helps security analysts and students gather information about a target domain or IP address through various scanning techniques and generates reports for analysis.

This project was developed as part of a Cybersecurity Internship to demonstrate practical knowledge of network scanning, information gathering, and Python programming.

---

## Features

- Host Discovery
- Port Scanning
- DNS Lookup
- WHOIS Lookup
- Nmap Scan
- Automatic Report Generation
- Menu-Driven Command Line Interface
- Run All Option (Single Target Input)

---

## Technologies Used

- Python 3
- Nmap
- Socket Programming
- WHOIS Library
- DNS Resolver
- Subprocess Module
- Kali Linux / Ubuntu
- Visual Studio Code

---

## Project Structure

```
Network-Reconnaissance/
│
├── scripts/
│   ├── host_discovery.py
│   ├── port_scanner.py
│   ├── dns_lookup.py
│   ├── whois_lookup.py
│   └── nmap_scan.py
│
├── reports/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/network-reconnaissance-tool.git
```

Move into the project folder:

```bash
cd network-reconnaissance-tool
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## How to Run

Run the main program:

```bash
python3 main.py
```

or

```bash
python main.py
```

---

## Menu Options

1. Host Discovery
2. Port Scanner
3. DNS Lookup
4. WHOIS Lookup
5. Nmap Scan
6. Run All Modules
0. Exit

---

## Sample Output

```
=============================
Network Reconnaissance Tool
=============================

1. Host Discovery
2. Port Scanner
3. DNS Lookup
4. WHOIS Lookup
5. Nmap Scan
6. Run All
0. Exit

Enter your choice:
```

---

## Reports

The generated reports are automatically stored inside the **reports/** folder for future reference.

---

## Learning Outcomes

This project helped in understanding:

- Network Reconnaissance
- Information Gathering
- Port Scanning
- DNS Resolution
- WHOIS Information
- Nmap Scanning
- Python Automation
- Cybersecurity Fundamentals
- Report Generation
- Modular Programming

---

## Future Enhancements

- Multi-threaded Port Scanner
- Service Version Detection
- OS Fingerprinting
- Vulnerability Assessment
- PDF Report Generation
- Web Dashboard using Flask
- Database Integration
- Scan History Management

---

## Author

**Dharanish**

Cybersecurity Internship Project

---

## License

This project is developed for educational and learning purposes.
