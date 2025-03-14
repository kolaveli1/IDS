from collections import defaultdict
from scapy.all import sniff, IP, TCP
from database import log_attack 

INTERFACE = "en0"
PORT_SCAN_THRESHOLD = 10  

scan_attempts = defaultdict(int)

def detect_scan(packet):
    if packet.haslayer(TCP) and packet[TCP].flags == "S": 
        scan_attempts[packet[IP].src] += 1
        if scan_attempts[packet[IP].src] > PORT_SCAN_THRESHOLD:
            log_attack("Port Scan", packet[IP].src, "Mange SYN-pakker sendt")


sniff(prn=detect_scan, store=0, iface=INTERFACE)
