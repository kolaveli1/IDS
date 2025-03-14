# IDS
This project is a simple Network Intrusion Detection System (IDS) that monitors network traffic, detects suspicious activity, and logs attacks in a SQLite database. It also provides a Flask-based web interface to view detected attacks in real-time.

The IDS consists of multiple Python scripts that:
1. Sniff network traffic using scapy.
2. Detect various types of attacks, including:
    - Port Scanning (e.g., from nmap)
    - DDoS Attacks (excessive requests per second)
    - Man-in-the-Middle (MITM) Attacks (ARP spoofing)
3. Log detected attacks in an SQLite database.
4. Display attack logs in a Flask-based web interface.


1) Port Scanning
Attackers scan for open ports on a system to find vulnerabilities. This IDS detects multiple SYN packets from the same IP.
Detection Logic:
    - Monitors TCP SYN packets.
    - If an IP sends 10+ SYN packets without completing a connection, it’s flagged as a Port Scan.
To test it, run the following from another machine:
nmap -p 1-1000 <yourIP>


2) DDos Detection
A DDos attack is when an attacker overloads a target by sending a large number of requests in a short time.
Detection Logic:
    - Counts the number of packets per second from each IP.
    - If an IP sends 100+ packets per second, it is flagged as a DDoS attack.
To test it, run a TCP flood from another machine:
hping3 -S --flood -p 80 <yourIP>


3) MITM Detection
A Man-in-the-Middle (MITM) attack occurs when an attacker spoofs ARP messages to intercept network traffic.
Detection Logic:
    - Monitors ARP replies.
    - If an IP changes its MAC address frequently, it is flagged as a MITM attack.
To test it run arpspoof from another machine:
arpspoof -i en0 -t <victimIP> <gatewayIP>
- en0: Network interface (WIFI on macOS)
- <victimIP> IP address of target machine
- <gatewayIP> IP address of router
