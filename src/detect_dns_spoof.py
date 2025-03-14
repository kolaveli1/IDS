from scapy.all import sniff, DNS, IP
from database import log_attack


def detect_dns_spoof(packet):
    if packet.haslayer(DNS) and packet.haslayer(IP):
        log_attack("DNS Spoofing", packet[IP].src, "Mistænkelig DNS-pakke opdaget")

sniff(prn=detect_dns_spoof, store=0, iface="en0")
