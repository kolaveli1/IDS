from collections import defaultdict
from time import time
from scapy.all import sniff, IP
from database import log_attack

INTERFACE = "en0"
DDOS_THRESHOLD = 100

packet_counts = defaultdict(int)
start_time = time()

def detect_ddos(packet):
    global start_time
    if packet.haslayer(IP):
        packet_counts[packet[IP].src] += 1

        if time() - start_time > 1:
            for ip, count in packet_counts.items():
                if count > DDOS_THRESHOLD:
                    log_attack("DDoS", ip, f"{count} pakker/s")
            packet_counts.clear()
            start_time = time()


sniff(prn=detect_ddos, store=0, iface=INTERFACE)
