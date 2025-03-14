from scapy.all import sniff, ARP
from database import log_attack

def detect_arp_spoof(packet):
    if packet.haslayer(ARP) and packet[ARP].op == 2:
        log_attack("MITM Attack", packet[ARP].psrc, f"MAC: {packet[ARP].hwsrc}")

sniff(prn=detect_arp_spoof, store=0, iface="en0")
