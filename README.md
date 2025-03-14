# IDS
This project is a simple Network Intrusion Detection System (IDS) that monitors network traffic, detects suspicious activity, and logs attacks in a SQLite database. It also provides a Flask-based web interface to view detected attacks in real-time.

The IDS consists of multiple Python scripts that:

1. Sniff network traffic using `scapy`.
2. Detect various types of attacks, including:
    - **Port Scanning** (e.g., from `nmap`)
    - **Man-in-the-Middle (MITM) Attacks** (ARP spoofing)
    - **DDoS Attacks** (excessive requests per second)
3. Log detected attacks in an SQLite database.
4. Display attack logs in a Flask-based web interface.

---

## **1) Port Scanning**
Attackers scan for open ports on a system to find vulnerabilities. This IDS detects multiple SYN packets from the same IP.

### **Detection Logic:**
- Monitors **TCP SYN packets**.
- If an IP sends **10+ SYN packets** without completing a connection, it’s flagged as a **Port Scan**.

### **How to test it:**
Run the following from another machine:
```bash
nmap -p 1-1000 <yourIP>
```

---

## **2) MITM Detection**
A **Man-in-the-Middle (MITM) attack** occurs when an attacker spoofs ARP messages to intercept network traffic.

### **Detection Logic:**
- Monitors **ARP replies**.
- If an IP **changes its MAC address frequently**, it is flagged as a **MITM attack**.

### **How to test it:**
Run `arpspoof` from another machine:
```bash
arpspoof -i en0 -t <victimIP> <gatewayIP>
```
- **`en0`**: Network interface (WIFI on macOS)
- **`<victimIP>`**: IP address of target machine
- **`<gatewayIP>`**: IP address of router

---

## **3) DDoS Detection**
A **DDoS attack** occurs when an attacker overloads a target by sending a large number of requests in a short time.

### **Detection Logic:**
- Counts **the number of packets per second** from each IP.
- If an IP sends **100+ packets per second**, it is flagged as a **DDoS attack**.

### **How to test it:**
Run a TCP flood from another machine:
```bash
hping3 -S --flood -p 80 <yourIP>
```

---

## **Running the IDS**
### **Run all detection modules at once**
Use the `run_all.py` script to start everything:
```bash
python3 src/run_all.py
```
This will launch:
**Port Scanning Detection**  
**MITM (ARP Spoofing) Detection**  
**DDoS Detection**  

### **Run the Web UI**
To view detected attacks, start the Flask server:
```bash
python3 server.py
```
Then open **[http://localhost:3000](http://localhost:3000)** in your browser.

---

